from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic1}",
    input_variables=["topic1"]
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post on {topic2}",
    input_variables=["topic2"]
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2, model, parser)
}) # will return a dictionary with keys as tweet and linkedin

result = parallel_chain.invoke({"topic1": "AI", "topic2": "GenAI"})

print("***********Tweet**************")
print(result["tweet"])
print("************Linkedin Post**************")
print(result["linkedin"])