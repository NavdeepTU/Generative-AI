from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct") # used very less now, ChatModels are now used more

result = llm.invoke("What is the capital of India?")

print(result)