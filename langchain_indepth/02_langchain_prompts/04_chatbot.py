from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(chat_history) # can take in list of messages as well
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history) 
# this chat history list contains all the previous
# conversation but does not contains info that who said what.
# This info is important for the chatbot to output relevent results