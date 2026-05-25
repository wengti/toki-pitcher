import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel

from data.db_client import create_supabase_client
from model.model import CustomerDataModel, PitcherPromptModel
from postgrest.exceptions import APIError

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
                cur_plan_data = data
            elif data["name"] == new_plan_name:
                new_plan_data = data

        if cur_plan_data == None or new_plan_data == None:
            raise HTTPException(
                status_code=500,
                detail="Unable to retrieve the plan details.",
            )

        # Convert data into template dict

        # Invoke the LLM chain

        # Update database

        # Send the response back

    except HTTPException as error:
        raise

    except APIError as error:
        raise HTTPException(status_code=500, detail=str(error))

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
