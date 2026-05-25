import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)


def create_pitcher_chain():

    # System prompt provides an overview of the task
    with open("ai/pitcher_system_prompt.txt", "r") as f:
        system_prompt = f.read()

    # Human Message provides
    # details of customer, current plan and suggested plan to renew to
    with open("ai/human_message_prompt.txt", "r") as f:
        human_message_template = f.read()

    template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            ("human", human_message_template),
        ]
    )

    # Use a temperature of 0.2, allowing the model to
    # generate slighly more varied and more personalised pitch
    model = init_chat_model(
        model=os.getenv("MODEL_NAME"),
        temperature=0.2,
    )

    return template | model
