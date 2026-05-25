import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel

from ai.pitcher_chain import create_pitcher_chain
from data.db_client import create_supabase_client
from model.model import CustomerDataModel, PitcherPromptModel
from postgrest.exceptions import APIError

from model.supabase_model import PublicPlans

load_dotenv(override=True)

app = FastAPI()

origins = [
    os.getenv("FRONTEND_URL"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/pitch")
def generate_pitch(customer_data: CustomerDataModel):

    try:
        # Decide plan to be suggested
        monthly_usage = customer_data.monthly_usage
        cur_plan_name = customer_data.plan

        if monthly_usage < 200:
            new_plan_name = "Tier 4"
        elif monthly_usage < 400:
            new_plan_name = "Tier 3"
        elif monthly_usage < 600:
            new_plan_name = "Tier 2"
        else:
            new_plan_name = "Tier 1"

        # Fetch plan details
        supabase = create_supabase_client()
        response = (
            supabase.table("plans")
            .select("*")
            .or_(f"name.eq.{cur_plan_name},name.eq.{new_plan_name}")
            .execute()
        )

        cur_plan_data = None
        new_plan_data = None
        for data in response["data"]:
            if data["name"] == cur_plan_name:
                cur_plan_data = PublicPlans(data)
            elif data["name"] == new_plan_name:
                new_plan_data = PublicPlans(data)

        if cur_plan_data == None or new_plan_data == None:
            raise HTTPException(
                status_code=500,
                detail="Unable to retrieve the plan details.",
            )

        # Convert data into template dict
        pitcher_template_dict = PitcherPromptModel(
            customer_name=customer_data.name,
            tenure_start=customer_data.tenure_start,
            tenure_end=customer_data.tenure_end,
            monthly_usage=str(customer_data.monthly_usage),
            cur_plan_name=customer_data.plan,
            cur_plan_price=str(cur_plan_data.plan_price),
            cur_download_speed=str(cur_plan_data.download_speed),
            cur_upload_speed=str(cur_plan_data.upload_speed),
            new_plan_name=new_plan_data.name,
            new_plan_price=str(new_plan_data.plan_price),
            new_download_speed=str(new_plan_data.download_speed),
            new_upload_speed=str(new_plan_data.upload_speed),
            new_plan_duration_months=str(new_plan_data.plan_duration_months),
            router=new_plan_data.router,
            mesh_price=f"RM {new_plan_data.mesh_price} per month",
            fttr_price=(
                f"RM {new_plan_data.fttr_price} per month"
                if new_plan_data.fttr_price is not None
                else None
            ),
            promotion=(
                f"RM {new_plan_data.plan_price_promo} for the first 6 months"
                if new_plan_data.plan_price_promo is not None
                else None
            ),
        ).model_dump()

        # Invoke the LLM chain
        pitcher_chain = create_pitcher_chain()
        ai_response = pitcher_chain.invoke(pitcher_template_dict)
        ai_answer = ai_response.content

        # Update database
        update_response = (
            supabase.table("customers")
            .update({"pitch": ai_answer})
            .eq("id", customer_data.id)
            .execute()
        )

        # Send the response back

    except HTTPException as error:
        raise

    except APIError as error:
        raise HTTPException(status_code=500, detail=str(error))

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
