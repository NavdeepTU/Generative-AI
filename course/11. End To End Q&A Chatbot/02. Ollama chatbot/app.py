import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
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
    llm = Ollama(model=llm)
    # create an output parser to handle the model's response
    output_parser = StrOutputParser()
    # create a chain: prompt -> llm -> parser
    chain = prompt | llm | output_parser
    # generate the response
    answer = chain.invoke({"question":question})
    return answer

# application interface
# title of the app
st.title("Enhanced Q&A Chatbot With OpenAI")
# sidebar controls
llm = st.sidebar.selectbox("Select Open Source model", ["llama3.2"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)
# main interface
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide the user input")