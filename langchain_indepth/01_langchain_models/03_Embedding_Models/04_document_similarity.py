from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is known for his aggressive batting and unmatched consistency across all formats of cricket.",
    "Sachin Tendulkar, often called the 'God of Cricket,' holds numerous records, including 100 international centuries.",
    "Rohit Sharma, the 'Hitman' of Indian cricket, is renowned for his effortless six-hitting and multiple double centuries in ODIs.",
    "Jasprit Bumrah is India's pace spearhead, famous for his deadly yorkers and unorthodox bowling action.",
    "MS Dhoni, the legendary captain, led India to multiple ICC trophies and is admired for his cool-headed leadership and finishing ability."
]

query = "tell me about Bumrah"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0] # both embeddings are 2-D list

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1] # getting the last score as its value is highest

print(query)
print(documents[index])
print("similarity score is: ", score)


# storing text in the form of vectors is helpful to get 
# similarity values

# we are not storing these embeddings somewhere, 
# everytime we have to generate embeddings
# need to store it somewhere
# will understand it in RAGs

