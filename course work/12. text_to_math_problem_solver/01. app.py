import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

# set up the streamlit app
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant", page_icon="🧮")
st.title("Text to Math Problem Solver using Google Gemma 2")

groq_api_key = st.sidebar.text_input(label="Groq API Key", type="password")

if not groq_api_key:
    st.info("Please add your Groq API key to continue")
    st.stop()

llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# initializing the tools
wikipedia_wraper = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name="Wikipedia",
    func=wikipedia_wraper.run,
    description="A tool for searching the Internet to find the various information on the topics mentioned"
)

# initialize the math tool
math_chain = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering math related questions. Only input mathematical expression need to be provided."
)

prompt = """
You are a agent tasked for solving users mathematical questions. 
Logically arrive at the solution and provide a detailed explanation
and display it point wise for the question below
Question:{question}
Answer:
"""

prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

# combine all the tools into chain
chain = LLMChain(llm=llm, prompt=prompt_template)
reasoning_tool = Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic based and reasoning questions."
)

# initialize the agents

assistant_agent = initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handling_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"assistant", "content":"Hi, I am a Math chatbot who can answer all your math questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Let us start the interaction
question = st.text_area("Enter your question:", "I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user", "content":question})
            st.chat_message("user").write(question)

            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role":"assistant", "content":response})
            st.write("### Reaponse:")
            st.success(response)
    else:
        st.warning("Please enter the question")