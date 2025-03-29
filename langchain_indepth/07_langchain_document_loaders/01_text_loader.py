from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write the summary for the following poem\n{poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

print(docs)

# [Document(metadata={'source': 'cricket.txt'}, 
#           page_content='Cricket – A Gentleman’s Game\n\nBeneath the sun, on fields so wide,\nWhere willow meets the leather’s stride.\nA game of grace, of skill and might,\nWhere dreams take flight in morning light.\n\nThe bowler steams with fire and pace,\nA perfect line, a deadly chase.\nThe batsman stands, so calm, so tall,\nAwaiting fate, to rise or fall.\n\nA flick, a drive, a soaring six,\nThe crowd erupts, their hearts transfixed.\nA diving catch, a stumping neat,\nMoments that make the game complete.\n\nThe sound of cheers, the echoing roars,\nThe battle fought in runs and scores.\nThrough highs and lows, in sun or rain,\nCricket’s spirit will never wane.\n\nFor young and old, it weaves a spell,\nA timeless tale, we know so well.\nA game of honor, fierce yet fair,\nWith passion’s fire beyond compare.')]

print(type(docs)) # python list

print(len(docs)) # 1

print(docs[0])

print(type(docs[0])) # <class 'langchain_core.documents.base.Document'>

print(docs[0].page_content) # can convert this extraction into runnable using Runnable Lambda and add it to the below chain

print(docs[0].metadata) # {'source': 'cricket.txt'}

chain = prompt | model | parser

result = chain.invoke({"poem": docs[0].page_content})

print(result)