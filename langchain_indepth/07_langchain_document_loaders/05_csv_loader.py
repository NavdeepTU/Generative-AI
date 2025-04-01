from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Social_Network_Ads.csv") # can use lazy loading if file is very large

docs = loader.load()

print(len(docs)) # every row is treated as a document object

print(docs[0])

# page_content='User ID: 15624510
# Gender: Male
# Age: 19
# EstimatedSalary: 19000
# Purchased: 0' metadata={'source': 'Social_Network_Ads.csv', 'row': 0}