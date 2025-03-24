from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=["text"]
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "cricket"})

print(result)

# {'joke': 'Why did the cricket team go to the bank?\nTo improve their bowling average!', 
#  'explanation': 'This joke plays on the double meaning of the phrase "bowling average." 
#                  In cricket, a bowling average refers to the number of runs a bowler concedes per wicket taken. 
#                  However, in a more general sense, a bowling average can also refer to the average score a player 
#                  achieves in a game of bowling. The joke suggests that the cricket team went to the bank to improve 
#                  their bowling average in the sense of their performance in a game of bowling, rather than their performance on the cricket field.'}