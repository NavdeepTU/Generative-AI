from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about the {topic} \n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# method 1
prompt = template.invoke({"topic": "black hole"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

# method 2
chain = template | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)

# {'fact_1': 'A black hole is a region in space where the gravitational pull is so strong that nothing, not even light, can escape from it.', 
#  'fact_2': 'Black holes can form from the remnants of massive stars that have reached the end of their life cycle.', 
#  'fact_3': 'The boundary surrounding a black hole, beyond which nothing can escape, is called the event horizon.'}

# can only define schema but cannot do validation.