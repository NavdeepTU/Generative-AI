import json
import os
import sys
import boto3

# using Titan embeddings model to generate embedding
from langchain_community.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock

# data ingestion
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Vector Embedding and Vector Store
from langchain.vectorstores import FAISS

# llm models
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA 

# bedrock clients
bedrock = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock)

# data ingestion
def data_ingestion():
    loader = PyPDFDirectoryLoader("data")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    docs = text_splitter.split_documents(documents)
    return docs

# Vector embedding and vector store
def get_vector_store(docs):
    vectorstore_faiss = FAISS.from_documents(
        docs,
        bedrock_embeddings
    )
    vectorstore_faiss.save_local("faiss_index")

def get_claude_llm():
    # create the anthropic model
    llm = Bedrock(model_id="ai21.j2-mid-v1", client=bedrock,
                  model_kwargs={"maxTokens":512})
    return llm

def get_llama2_llm():
    # create the llama2 model
    llm = Bedrock(model_id="meta.llama2-70b-chat-v1", client=bedrock,
                  model_kwargs={"max_gen_len":512})
    return llm

prompt_template = """
Human: Use the following pieces of context to provide a 
concise answer to the question at the end but use atleast summarize 
with 250 words with detailed explaantions. If you don't know the answer, 
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context

Question: {question}

Assistant:
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

def get_response_llm(llm, vectorstore_faiss, query):
    pass