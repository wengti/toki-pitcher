import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)


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
