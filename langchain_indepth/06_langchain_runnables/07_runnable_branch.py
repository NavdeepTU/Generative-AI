from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnableBranch, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text\n{text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch( 
    (lambda x: len(x.split()) > 300, prompt2 | model | parser),
    RunnablePassthrough()
) # 

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke({"topic": "Russia Vs Ukraine"})

print(result)