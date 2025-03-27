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
        start_time = time.time()
        template = """Use the following pieces of context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Always say "คร้าบเจ้านาย" at the end of the answer.

        {context}

        Question: {question}

        Helpful Answer:"""
        custom_rag_prompt = PromptTemplate.from_template(template)
        print(f"Create Prompt in {time.time()-start_time:.2f}s")
        return custom_rag_prompt
    
# template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
# {context}
# Question: {question}
# Helpful Answer:"""
# QA_CHAIN_PROMPT = PromptTemplate.from_template(template)