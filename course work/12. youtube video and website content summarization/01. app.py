import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains. summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# streamlit app
st.set_page_config(page_title="LangChain: Summarize Text From YT oe Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

# Get the groq api key and url (YT or website) to be summarized
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

if st.button("Summarize the Content from YT oe Website"):
    # validate all the inputs
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid url. It can may be a YT video url or website url")
    else:
        try:
            with st.spinner("Waiting..."):
                # loading the website or yt video data