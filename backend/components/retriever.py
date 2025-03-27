from langchain.retrievers import SelfQueryRetriever
from langchain_openai import ChatOpenAI
from langchain.chains.query_constructor.schema import AttributeInfo
import time

from components.embedding import Embed as emb

class Retriever():
    def __init__(self):
        pass
    def CreateRetriever(self, vectordb):
        start_time = time.time()
        metadata_field_info = [
            AttributeInfo(name="year", description="The year of the document", type="string"),
            AttributeInfo(name="company", description="The company of the document", type="string"),
            AttributeInfo(name="part", description="The part one or two of the document", type="integer"),
            AttributeInfo(name="Category", description="The category of the document", type="string"),
            AttributeInfo(name="Risk_Detail", description="The risk detail of the document", type="string"),
            AttributeInfo(name="Risk_Topic", description="The risk topic of the document", type="string"),
        ]

        retriever = SelfQueryRetriever.from_llm(
            llm=ChatOpenAI(),
            vectorstore=vectordb,
            document_contents="Documents about various type of risks in many companies",
            metadata_field_info=metadata_field_info,
            # enable_limit= True
        )
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"Retrieving completed in {elapsed_time:.2f} seconds")
        return retriever