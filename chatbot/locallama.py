# -------------------- TASK 2 ------------------------- #

from langchain_openai import ChatOpenAI
from  langchain_core.prompts import ChatPromptTemplate # template for outputs
from langchain_core.output_parsers import StrOutputParser # output parsor for the LLM output / split / capitalzied 
import streamlit as st
import os 
from dotenv import load_dotenv

# import llama model from langchain

from langchain_community.llms import Ollama

load_dotenv()

os.environ['LANGCHAIN_ENDPOINT'] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_kEY")
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
# Langsmith logging and audit
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv("LANGCHAIN_TRACING_V2")


## prompt template 

prompt = ChatPromptTemplate.from_messages(

    [
        ("system" , "You are a helpful assistant. Please respond to the user queries."),
        ("user" , "Question:{question}")
    ]
)

## Streamlit Framework

st.title('Langchain Demo with Ollama API') # To call open source models
input_text = st.text_input("Search for the topic you want to research (No Cost :) )- ")


## Call the Open source models

llm = Ollama(model="llama3")
output_parser = StrOutputParser() # object to receive the output from the llm

## Next step is to couple these items into chain . Prompt + llm + output parser

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text})) 

