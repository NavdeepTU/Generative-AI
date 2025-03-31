from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("temp.pdf")

docs = loader.load()

print(docs)

print(len(docs)) # 15 (because we have 15 pages in the pdf document)

print(docs[0].page_content)

print(docs[0].metadata)