from langchain_core.prompts import ChatPromptTemplate


def create_pitcher_chain():

    with open("/ai/pitcher_system_prompt.txt", "r") as f:
        system_prompt = f.read()

    with open("/ai/human_message_prompt.txt", "r") as f:
        human_message_template = f.read()

    template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            ("human", human_message_template),
        ]
    )
