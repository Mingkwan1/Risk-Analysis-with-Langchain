from langchain_core.prompts import HumanMessagePromptTemplate, AIMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
import time

class Prompt:
    def __init__(self):
        pass
    def create_prompt(self):
        # Define the system message template
        # system_template = """End every answer with "คร้าบเจ้านาย". Use the data you have as context to answer the users question. Use the chat history as additional context to answer the users question. 
        # If you cannot find the answer from the pieces of context, just say that you don't know, don't try to make up an answer.
        # ----------------
        # """

        # # Create the chat prompt templates
        # messages = [
        # SystemMessagePromptTemplate.from_template(system_template),
        # HumanMessagePromptTemplate.from_template("{question}")
        # ]

        # qa_prompt = ChatPromptTemplate.from_messages(messages)

        # return qa_prompt
        # start_time = time.time()
        #1.) Persona
        #2.) Task
        #3.) Input Information
        template = """
        You are an expert risk analyst for corporate clients. 
        You have knowledge in financial, operational, strategic risk analysis and are able to provide insights on risk reports.
        You understand the yearly context of each year and the financial situation in each year.
        You can give  a summarization, speculation, or analysis of the yearly risk report.

        Use the following pieces of context to answer the question at the end.
        Your context will be a yearly risk report from corporation
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Return a statement with atleast 600 words with details.

        The input you will receive is a risk analysis question from a corporate client.
        Always say "คร้าบเจ้านาย" at the end of the answer.

        {context}

        Question: {question}

        Helpful Answer:"""
        custom_rag_prompt = PromptTemplate.from_template(template)
        # print(f"Create Prompt in {time.time()-start_time:.2f}s")
        return custom_rag_prompt
    
# template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
# {context}
# Question: {question}
# Helpful Answer:"""
# QA_CHAIN_PROMPT = PromptTemplate.from_template(template)