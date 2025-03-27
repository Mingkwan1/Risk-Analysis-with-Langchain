from components.embedding import Embed as emb
from components.retriever import Retriever as retri

vectordb = emb().load_cached()
retriever = retri().CreateRetriever(vectordb)