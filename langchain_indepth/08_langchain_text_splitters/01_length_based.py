from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("acsbr-017.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0,
    separator=""
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)

print(type(chunks)) # list

print(type(chunks[0])) # document object

print(len(chunks)) # 326