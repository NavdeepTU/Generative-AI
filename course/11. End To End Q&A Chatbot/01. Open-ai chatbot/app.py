import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With OPENAI"

# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# response generation function
def generate_response(question, api_key, engine, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question':question})
    return answer

# streamlit web app setup
st.title("Enhanced Q&A Chatbot With OpenAI")
# sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Open AI API Key:", type="password")
engine = st.sidebar.selectbox("Select Open AI model", ["gpt-4o", "gpt-4-turbo", "gpt-4"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)
# main interface
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")
# response logic
if user_input and api_key:
    response = generate_response(user_input, api_key, engine, temperature, max_tokens)
    st.write(response)
elif user_input:
    st.warning("Please enter the OpenAI API Key in the sidebar")
else:
    st.write("Please provide the user input")