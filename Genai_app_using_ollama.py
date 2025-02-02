import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')

# prompt template

prompt=ChatPromptTemplate.from_messages(
        [
            ("system","You are helpful assistant.Please respond to the question asked"),
            ("user","Question:{question}")
        ]
)

# streamlit framework

st.title("Langchin Demo with Gemma")
input_text=st.text_input("What question you have in my mind?")

llm=Ollama(model='gemma2')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

# result=chain.invoke({"question":'What is Gen AI?'})
# print(result)
# input_text='What is Gen AI?'