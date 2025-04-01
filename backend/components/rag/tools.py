from langchain_core.tools import tool
from components.embedding import Embed as emb
from components.retriever import Retriever as retri

vectordb = emb().load_cached()
retriever = retri().CreateRetriever(vectordb)

@tool(response_format="content_and_artifact")
def retrieve(query: str):
    """Retrieve information related to a query."""
    retrieved_docs = retriever.invoke(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

retrieve = retrieve