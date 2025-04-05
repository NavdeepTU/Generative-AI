from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample = """
Farmers were working hard in the fields, 
preparing the soil and planting seeds for the next season. 
The sun was bright, and the air smelled of earth and fresh 
grass. The Indian Premier League (IPL) is the biggest 
cricket league in the world. People all over the world 
watch the matches and cheer for their favourite teams.


Terrorism is a big danger to peace and safety. It causes 
harm to people and creates fear in cities and villages. 
When such attacks happen, they leave behind pain and sadness. 
To fight terrorism, we need strong laws, alert security 
forces, and support from people who care about peace and 
safety.
"""

docs = text_splitter.create_documents([sample])

print(len(docs)) # 3

print(docs)

# [Document(metadata={}, page_content='\nFarmers were working hard in the fields, \npreparing the soil and planting seeds for the next season.'), 
#  Document(metadata={}, page_content='The sun was bright, and the air smelled of earth and fresh \ngrass. The Indian Premier League (IPL) is the biggest \ncricket league in the world. People all over the world \nwatch the matches and cheer for their favourite teams.'), 
#  Document(metadata={}, page_content='Terrorism is a big danger to peace and safety. It causes \nharm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security \nforces, and support from people who care about peace and \nsafety. ')]