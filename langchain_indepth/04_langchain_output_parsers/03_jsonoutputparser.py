from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n{format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()} # partial because filled before runtime
)

# method 1
prompt = template.format()

# print(prompt)

# Give me the name, age and city of a fictional person 
# Return a JSON object.

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
print(type(final_result)) # dict, python treats json objects as dictionaries

# method 2
chain = template | model | parser # everything is happening automatically

result = chain.invoke({})

print(result)

# {'name': 'Emily Johnson', 'age': 30, 'city': 'Los Angeles'}