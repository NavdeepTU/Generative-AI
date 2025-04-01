from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs)) # total number of pages in all the documents

# print(docs[0].page_content)

# print(docs[0].metadata)

for document in docs:
    print(document.metadata)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)