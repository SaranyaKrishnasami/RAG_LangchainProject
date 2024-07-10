# This is to create API's for the chat models - Libraries 
# Web / Mobile -> API -> Route -> OpenAImodel / Llama model

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
 
from langchain_community.llms import Ollama
from langserve import add_routes # differet routes to interact with different models 
import uvicorn
import os
from dotenv import load_dotenv
from langchain_community.llms import ollama
from langchain_community.llms import openai
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") 

# Create Fast API 

app = FastAPI(
 title = "Langchain_Server",
 version = "1.0",
 description= "API Server Demo1"
)

#

model = ChatOpenAI()
# ollama llama2
 
llm = Ollama(model="llama3")
 

prompt1 = ChatPromptTemplate.from_template("Write an essay about  {topic} with 50 words") # Open AI model
prompt2 = ChatPromptTemplate.from_template("Write a poem about  {topic} with 50 words")  # llama model

add_routes(
    app,
    prompt1 | model ,
    path="/essay"
)
add_routes(
    app,
    prompt2 | llm ,
    path="/poem"
)


if __name__ == "__main__":
    uvicorn.run(app , host="localhost" , port = 8000)