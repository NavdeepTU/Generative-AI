from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

class CollegeNames(BaseModel):

    name1: str = Field(description="Name of the first college")
    name2: str = Field(description="Name of the second college")
    name3: str = Field(description="Name of the third college")
    name4: str = Field(description="Name of the fourth college")
    name5: str = Field(description="Name of the fifth college")

model = ChatOpenAI()
parser = PydanticOutputParser(pydantic_object=CollegeNames)
template = PromptTemplate(
    template="Generate names of top 5 {location} colleges.\n {format_instruction}",
    input_variables=["location"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

names_chain = RunnableSequence(template, model, parser)
result = names_chain.invoke({"location": "american"})
print(result.name1)
print(result.name2)
print(result.name3)
print(result.name4)
print(result.name5)
