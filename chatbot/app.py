# Step 1 : Created a folder in the VScode - Uploading it from the folder 'LANGCHAIN'
# Step 2 : Create a virtaul environment with the command - python -m venv .venv  
# Step 3 : Create a file in the Root of the folder 'LANGCHAIN' as .env file
# Run the command 'pip install python-dotenv' in the terminal
# Code from Krish file - https://github.com/krishnaik06/Updated-Langchain/blob/main/chatbot/app.py

# Check if the code is running in the virtual environment - ( We should see the  (.venv) near to the command prompt in the terminal )
# IF we do not see it then in terminal do the below two commands
# Command 1 to be in the (.venv): Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# and then Command 2 be in the (.venv): .\.venv\Scripts\activate

# -------------------- TASK 1 ------------------------- #
# Building conversational 
# Install all the Dependant libraries
 
from langchain_openai import ChatOpenAI
from  langchain_core.prompts import ChatPromptTemplate # template for outputs
from langchain_core.output_parsers import StrOutputParser # output parsor for the LLM output / split / capitalzied 
import streamlit as st
import os 
from dotenv import load_dotenv


## Set Environmen Variables
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


st.title('Langchain Demo with OPENAI  API')
input_text = st.text_input("Search for the topic you want to research - ")


## Call OPENAI LLM

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser() # object to receive the output from the llm

## Next step is to couple these items into chain . Prompt + llm + output parser

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question' : input_text})) 



