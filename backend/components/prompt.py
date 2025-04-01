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

    def systemMessage(self, docs_content):
        # Define the system message template
        system_template = """

        You are an expert risk analyst for corporate clients. 
        You have knowledge in financial, operational, strategic risk analysis and are able to provide insights on risk reports.
        You understand the yearly context of each year and the financial situation in each year.
        You can give  a summarization, speculation, or analysis of the yearly risk report.

        Use the following pieces of context to answer the question at the end.
        Your context will be a yearly risk report content from corporation
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Return a statement with atleast 150 words with details.

        Require Respond Structure
        1. Provide User for Risk Trend in 2023
            a. Question: What is most significant risk on FY2023
            b. Respond Structure:
                i. On FY2023, on Food and Beverage most significant risk contain with 1. XXXX 2. XXX and 3. XXX. Most concern risk is XXXX Risk because we found that this risk mention on Risk Management Report and Management Discussion and Analysis.
            c. Related control factor: 1. Business operation
            d. Optional Responding: 
                i. Table: table should be able to provide risk information include Risk category, risk detail, and related score to business operation. And this table should be group by risk impact to the company to allow user to considering on action and further plan.
                ii. Graph: graph should be contained with 2 graphs in at least, to describe (1) high risk that mention on the report to focus to related risk, (2) percentage for each risk that mention on the report to focus on risk. 
        2. Provide missing concern for user
            a. Question: (From User risk) What is risk that should be concern
            b. Respond Structure:
                i. From your current risk assessment, we suggest that you should concern on 1. XXXXX 2. XXXXXX and 3. XXXXX. Because this risk is mentioned on Risk Management Report and Management Discussion and Analysis.
            c. Related Control factor: 1. Business operation 2. Previous risk concern
            d. Optional Responding:
                i. Table: table should group significant risk to be focus on missing risk for user. 
        3. Risk suggestion
            a. Question: What which action that should do on risk treatment
            b. Respond Structure:
                i. From risk 1. XXXXX, we should treatment as XXXXXX 2. XXXXX, we should treatment as XXXXXX and 3. XXXXXX, we should treatment as XXXXXX.
            c. Related Control factor:
                
        
        The input you will receive is a risk analysis question from a corporate client.
        Always say "คร้าบเจ้านาย" at the end of the answer.
        """
        "\n\n"
        f"{docs_content}"
        
        
        return system_template