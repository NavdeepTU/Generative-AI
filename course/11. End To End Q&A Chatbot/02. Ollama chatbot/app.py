import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import ollama
import os
from dotenv import load_dotenv

load_dotenv()

# langsmith tracking setup
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"),
    ("user", "Question:{question}")
])

def generate_response(question, llm, temperature, max_tokens):
    # initialize the ollama model
    llm = ollama(model=llm)
    # create an output parser to handle the model's response
    output_parser = StrOutputParser()
    # create a chain: prompt -> llm -> parser
    chain = prompt | llm | output_parser
    # generate the response
    answer = chain.invoke({"question":question})
    return answer

