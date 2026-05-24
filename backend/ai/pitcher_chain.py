import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv(override=True)


class PitcherPromptModel(BaseModel):
    customer_name: str
    tenure_start: str
    tenure_end: str
    monthly_usage: str
    cur_plan_name: str
    cur_plan_price: str
    cur_download_speed: str
    cur_upload_speed: str
    new_plan_name: str
    new_plan_price: str
    new_download_speed: str
    new_upload_speed: str
    new_plan_duration_months: str
    router: str
    mesh_price: str | None
    fttr_price: str | None
    promotion: str | None


def create_pitcher_chain():

    with open("ai/pitcher_system_prompt.txt", "r") as f:
        system_prompt = f.read()

    with open("ai/human_message_prompt.txt", "r") as f:
        human_message_template = f.read()

    template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            ("human", human_message_template),
        ]
    )

    model = init_chat_model(
        model=os.getenv("MODEL_NAME"),
        temperature=0.2,
    )

    return template | model
