{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Missing some input keys: {'input', 'page_content'}",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[23], line 66\u001b[0m\n\u001b[1;32m     59\u001b[0m \u001b[38;5;66;03m# agent_executor.invoke({\"input\":user_query})\u001b[39;00m\n\u001b[1;32m     60\u001b[0m messages \u001b[38;5;241m=\u001b[39m [\n\u001b[1;32m     61\u001b[0m     {\n\u001b[1;32m     62\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrole\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124muser\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m     63\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcontent\u001b[39m\u001b[38;5;124m\"\u001b[39m: user_query\n\u001b[1;32m     64\u001b[0m     }\n\u001b[1;32m     65\u001b[0m ]\n\u001b[0;32m---> 66\u001b[0m \u001b[43msearch_agent\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43minvoke\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmessages\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/Desktop/Generative AI/Generative-AI/course work/09. search engine with langchain tools and agents/venv/lib/python3.12/site-packages/langchain/chains/base.py:170\u001b[0m, in \u001b[0;36mChain.invoke\u001b[0;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[1;32m    168\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mBaseException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m    169\u001b[0m     run_manager\u001b[38;5;241m.\u001b[39mon_chain_error(e)\n\u001b[0;32m--> 170\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m e\n\u001b[1;32m    171\u001b[0m run_manager\u001b[38;5;241m.\u001b[39mon_chain_end(outputs)\n\u001b[1;32m    173\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m include_run_info:\n",
      "File \u001b[0;32m~/Desktop/Generative AI/Generative-AI/course work/09. search engine with langchain tools and agents/venv/lib/python3.12/site-packages/langchain/chains/base.py:158\u001b[0m, in \u001b[0;36mChain.invoke\u001b[0;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[1;32m    151\u001b[0m run_manager \u001b[38;5;241m=\u001b[39m callback_manager\u001b[38;5;241m.\u001b[39mon_chain_start(\n\u001b[1;32m    152\u001b[0m     \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[1;32m    153\u001b[0m     inputs,\n\u001b[1;32m    154\u001b[0m     run_id,\n\u001b[1;32m    155\u001b[0m     name\u001b[38;5;241m=\u001b[39mrun_name,\n\u001b[1;32m    156\u001b[0m )\n\u001b[1;32m    157\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m--> 158\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_validate_inputs\u001b[49m\u001b[43m(\u001b[49m\u001b[43minputs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    159\u001b[0m     outputs \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m    160\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_call(inputs, run_manager\u001b[38;5;241m=\u001b[39mrun_manager)\n\u001b[1;32m    161\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m new_arg_supported\n\u001b[1;32m    162\u001b[0m         \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_call(inputs)\n\u001b[1;32m    163\u001b[0m     )\n\u001b[1;32m    165\u001b[0m     final_outputs: Dict[\u001b[38;5;28mstr\u001b[39m, Any] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprep_outputs(\n\u001b[1;32m    166\u001b[0m         inputs, outputs, return_only_outputs\n\u001b[1;32m    167\u001b[0m     )\n",
      "File \u001b[0;32m~/Desktop/Generative AI/Generative-AI/course work/09. search engine with langchain tools and agents/venv/lib/python3.12/site-packages/langchain/chains/base.py:290\u001b[0m, in \u001b[0;36mChain._validate_inputs\u001b[0;34m(self, inputs)\u001b[0m\n\u001b[1;32m    288\u001b[0m missing_keys \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mset\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39minput_keys)\u001b[38;5;241m.\u001b[39mdifference(inputs)\n\u001b[1;32m    289\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m missing_keys:\n\u001b[0;32m--> 290\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mMissing some input keys: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mmissing_keys\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mValueError\u001b[0m: Missing some input keys: {'input', 'page_content'}"
     ]
    }
   ],
   "source": [
    "from dotenv import load_dotenv\n",
    "from langchain_community.document_loaders import WebBaseLoader\n",
    "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
    "from langchain_openai import OpenAIEmbeddings\n",
    "from langchain_community.vectorstores import FAISS\n",
    "from langchain import hub # prompt template for agents\n",
    "from langchain_groq import ChatGroq\n",
    "from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun\n",
    "from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper\n",
    "from langchain.tools.retriever import create_retriever_tool\n",
    "# method1 to implement agents\n",
    "from langchain.agents import create_openai_tools_agent, AgentExecutor\n",
    "# method2 to implement agents\n",
    "from langchain.agents import initialize_agent, AgentType\n",
    "import os\n",
    "load_dotenv()\n",
    "\n",
    "# using the inbuilt tools of langchain - arxiv and wikipedia\n",
    "api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)\n",
    "arxiv_tool = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)\n",
    "\n",
    "api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)\n",
    "wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)\n",
    "\n",
    "# rag tool\n",
    "loader = WebBaseLoader(\"https://docs.smith.langchain.com\")\n",
    "docs = loader.load()\n",
    "document_chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)\n",
    "vectordb = FAISS.from_documents(documents=document_chunks, embedding=OpenAIEmbeddings())\n",
    "retriever = vectordb.as_retriever()\n",
    "retriever_tool = create_retriever_tool(retriever=retriever, name=\"langsmith-search\", description=\"Search any information about langsmith\")\n",
    "\n",
    "# web search tool\n",
    "web_search_tool = DuckDuckGoSearchRun(name=\"Web Search\") # to search from the internet\n",
    "\n",
    "# Toolbox\n",
    "tool_box = [wiki_tool, arxiv_tool, retriever_tool, web_search_tool]\n",
    "\n",
    "# run these tools with agents and llm models\n",
    "groq_api_key = os.getenv(\"GROQ_API_KEY\")\n",
    "llm = ChatGroq(groq_api_key=groq_api_key, model=\"Llama3-8b-8192\")\n",
    "\n",
    "# prompt template\n",
    "prompt = hub.pull(\"hwchase17/openai-functions-agent\")\n",
    "\n",
    "# method1 to implement agents\n",
    "# agent = create_openai_tools_agent(llm, tool_box, prompt)\n",
    "# agent executor\n",
    "# agent_executor = AgentExecutor(agent=agent, tools=tool_box, verbose=True)\n",
    "# user_query = \"What is an Agent?\"\n",
    "# agent_executor.invoke({\"input\":user_query})\n",
    "\n",
    "# method2 to implement agents\n",
    "search_agent = initialize_agent(tools=tool_box, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)\n",
    "\n",
    "\n",
    "# user_query = \"Tell me about agents in generativeAI\"\n",
    "# user_query = \"How many 3 pointers has Stephn curry made?\"\n",
    "user_query = \"What is an Agent?\"\n",
    "\n",
    "messages = [\n",
    "    {\n",
    "        \"role\": \"user\",\n",
    "        \"content\": user_query\n",
    "    }\n",
    "]\n",
    "search_agent.invoke(messages)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "What's the paper 1706.03762 about ?"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
