import os
from dotenv import load_dotenv

from components.load import Load as ld
from components.load import Split as split
from components.embedding import Embed as emb
from components.retriever import Retriever
from components.memory import Mem as mem
from components.prompt import Prompt as prm
from components.chain import Chain as chain
from components.rag.graph import Graph as graph

### 1.) Setting Up ###

# 1.1) Load Environment

load_dotenv() #

# 1.2) LangSmith Connection

# os.environ["LANGSMITH_TRACING"] = "true"
# os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
# os.environ["LANGSMITH_PROJECT"]="JuiceComRisk"

# 1.3) Loading the json file 

# risk_texts = ld().load()
# json_texts = ld().load_json()

# print(type(json_texts))
# print(json_texts[0])
# print(len(json_texts))

# print(type(risk_texts))
# print(risk_texts[0])
# print(len(risk_texts))

## 1.4) Splitting

# risk_texts = split().Rsplit(risk_texts)

# texts = split().jsonsplit(json_texts)

### 2.) Vector storing and Embedding ###

# vectordb = emb().load_cached()
# retriever = Retriever().CreateRetriever(vectordb)

query = "What are some financial risks of APURE in 2022?"
# ans = retriever.invoke(query)
# print(ans)

# prompt = prm().create_prompt()

# example_messages = prompt.invoke(
#     {"context": "(context goes here)", "question": "(question goes here)"}
# ).to_messages()

# assert len(example_messages) ==5 1
# print(example_messages[0].content)

# graph().show()
# graph().stream(query)
result = graph().generate(query)

# ### 3.) Retreival Q&A ###

#     ## 3.1) Memory

# # memory = mem().create_mem()

#     ## 3.2) Query


# print(retriever.invoke("hi"))

#     ## 3.3) Creating the chain
# qachain = chain()

#     ## 3.3) Running the chain
# result = qachain.Ans_QA(risk_texts, query, retriever, memory)

# def create_chain():
#     ### 1.) Loading Data ###
#     risk_texts = ld().load()

#     ### 2.) Vector storing and Embedding ###
#     vectordb = emb().emb(risk_texts=risk_texts)

#     ### 3.) Retrieval Q&A ###
#     memory = mem().create_mem()
#     query = "What are some financial risks of TVO in 2022?"

#     # Creating the chain
#     qachain = chain(query)

#     return qachain, vectordb, memory

# # Expose the chain as a global object
# qachain, vectordb, memory = create_chain()

# def Ans_QA(query: str):
#     return qachain.Ans_QA(query, vectordb, memory)

# if __name__ == "__main__":
#     print("hey")

### Creating a chatbot ###
