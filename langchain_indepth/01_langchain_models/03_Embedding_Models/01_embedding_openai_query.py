from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32) # more the dimension more info rich the vector

result = embedding.embed_query("Delhi is the capital of India") # embedding for single query

print(str(result))