import streamlit as st 
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Educate kids", page_icon=":robot:")
st.header("Hey, ask me anything and I will give out similar things")

embeddings = OpenAIEmbeddings()

from langchain_community.document_loaders.csv_loader import CSVLoader
loader = CSVLoader(file_path="myData.csv", csv_args={
    'delimiter': ',',
    'quotechar': '"',
    'fieldnames': ['Words']
})

data = loader.load()
print(data)