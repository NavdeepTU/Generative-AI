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