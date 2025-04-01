from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Answer the following question\n{question} from the following text\n{text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421?pid=COMH64PY76CJKBYU&lid=LSTCOMH64PY76CJKBYUOL7TOK&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=b1275c30-d1b7-4dfc-8980-93bcbee1931f.COMH64PY76CJKBYU.SEARCH&ppt=None&ppn=None&ssid=1smp87ukwzbh5q0w1743495078641"
loader = WebBaseLoader(url) # can also pass multiple urls, in that case content of each url will be stored in a different document

docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({
    "question": "What is the name of the product?",
    "text": docs[0].page_content
})

print(result)

# The name of the product is Apple MacBook AIR Apple M2 - (16 GB/256 GB SSD/macOS Sequoia) MC7X4HN/A.