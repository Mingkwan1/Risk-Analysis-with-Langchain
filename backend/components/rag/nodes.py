from components.rag.state import State
from components.load import Load as ld
from components.embedding import Embed as emb
from components.retriever import Retriever as retri
from components.prompt import Prompt as prompt
from langchain_openai import ChatOpenAI

import time

# risk_texts = ld().load()
vectordb = emb().load_cached()
retriever = retri().CreateRetriever(vectordb)
prompt = prompt().create_prompt()
# formatted_prompt = prompt.format(question = query)

def retrieve(state: State):
    retrieved_docs = retriever.invoke(state["question"])
    # retrieved_docs = vectordb.similarity_search(state["question"])
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    print("messages:", messages)
    llm=ChatOpenAI()
    response = llm.invoke(messages)
    return {"answer": response.content}
