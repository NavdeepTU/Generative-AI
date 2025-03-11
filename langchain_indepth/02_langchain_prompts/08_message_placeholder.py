from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []
# load chat history
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

# print(chat_history)

# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print(prompt)

# messages=[
# SystemMessage(content='You are a helpful customer support agent.', additional_kwargs={}, response_metadata={}), 
# HumanMessage(content='HumanMessage(content="I want to request a refund for my order #12345.")\n', additional_kwargs={}, response_metadata={}), 
# HumanMessage(content='AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")', additional_kwargs={}, response_metadata={}), 
# HumanMessage(content='Where is my refund?', additional_kwargs={}, response_metadata={})
# ]