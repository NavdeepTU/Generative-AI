import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain import hub # prompt template for agents
from langchain_groq import ChatGroq
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langchain.tools.retriever import create_retriever_tool
# method1 to implement agents
from langchain.agents import create_openai_tools_agent, AgentExecutor
# method2 to implement agents
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
load_dotenv()

# using the inbuilt tools of langchain - arxiv and wikipedia
api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv_tool = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)

# rag tool
loader = WebBaseLoader("https://docs.smith.langchain.com")
docs = loader.load()
document_chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
vectordb = FAISS.from_documents(documents=document_chunks, embedding=OpenAIEmbeddings())
retriever = vectordb.as_retriever()
retriever_tool = create_retriever_tool(retriever=retriever, name="langsmith-search", description="Search any information about langsmith")

# web search tool
web_search_tool = DuckDuckGoSearchRun(name="Web Search") # to search from the internet

# run these tools with agents and llm models
# groq_api_key = os.getenv("GROQ_API_KEY") # no need to fetch it from .env file, user will be providing it in the UI

# prompt template for the agent
# prompt = hub.pull("hwchase17/openai-functions-agent")

# method1 to implement agents
# agent = create_openai_tools_agent(llm, tool_box, prompt)
# agent executor
# agent_executor = AgentExecutor(agent=agent, tools=tool_box, verbose=True)
# user_query = "What is an Agent?"
# agent_executor.invoke({"input":user_query})

# User interface
st.title("Langchain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API key: ", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hi, I'm a chatbot who can search wikipedia, arxiv, some private documents and web as well. How can I help you?"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input(placeholder="What is Machine Learning?")

if prompt:
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=api_key, model="Llama3-8b-8192")
    # Toolbox
    tool_box = [wiki_tool, arxiv_tool, web_search_tool]
    # method2 to implement agents
    search_agent = initialize_agent(tools=tool_box, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

    with st.chat_message("assistant"):
        # This CallbackHandler is geared towards use with a LangChain 
        # Agent; it displays the Agent's LLM and tool-usage "thoughts" 
        # inside a series of Streamlit expanders.
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)