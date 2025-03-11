from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms, what is {topic}")
    # SystemMessage(content="You are a helpful {domain} expert."),  # this will not work due to weired behaviour
    # HumanMessage(content="Explain in simple terms, what is {topic}")
]) # can also use ChatPromptTemplate.from_messages -> same behaviour

prompt = chat_template.invoke({
    "domain": "cricket",
    "topic": "Dusra"
})

print(prompt)