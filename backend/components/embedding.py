from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers import SelfQueryRetriever
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Weaviate
from langchain_weaviate.vectorstores import WeaviateVectorStore
import weaviate

### 2.) Vector storing and Embedding ###

#2021_CFRESH file is in window1252
#2023 KBS have an error char, iNCOMPLETE BLACKET and no report year at the end

#Research more on vectordb!

class Embed:
    def __init__(self):
        pass
    #Embedding
    def emb(self, risk_texts):
        # Define metadata fields
        metadata_field_info = [
            AttributeInfo(name="year", description="The year of the document", type="string"),
            AttributeInfo(name="company", description="The company of the document", type="string"),
            AttributeInfo(name="part", description="The part one or two of the document", type="string"),
            AttributeInfo(name="Category", description="The category of the document", type="string"),
            AttributeInfo(name="Risk_Detail", description="The risk detail of the document", type="string"),
            AttributeInfo(name="Risk_Topic", description="The risk topic of the document", type="string"),
        ]
        self.risk_texts = risk_texts
        persist_directory = 'docs/chroma/'
        embedding = OpenAIEmbeddings()

        #Weaviate vectordb
        ### Check if this shit work
        # client = weaviate.connect_to_local()
        # client = weaviate.WeaviateClient(connection_config=weaviate.ConnectionConfig(
        # url="http://localhost:8080",  # Replace with your Weaviate instance URL
        # ))

        # weaviate_client = weaviate.connect_to_local()

        # vectordb = WeaviateVectorStore.from_documents(risk_texts, embedding, client=weaviate_client)

        # vectordb = Weaviate(client, "Document", "content", embedding=OpenAIEmbeddings())

            ###Chroma vectordb
        vectordb = Chroma.from_documents(documents= risk_texts,
                                  persist_directory=persist_directory, 
                                  embedding=embedding)
        retriever = vectordb
        return retriever

        # # Create the SelfQueryRetriever
        # retriever = SelfQueryRetriever.from_llm(
        #     llm=ChatOpenAI(),
        #     vectorstore=vectordb,
        #     document_contents="Documents about various type of risks in many companies",
        #     metadata_field_info=metadata_field_info,
        # )

        # client.close()  # Free up resources

        # return retriever

    def check(self, query):
        self.query = query
        # ans = vectordb.similarity_search(query,k=3)
        # # Print the results
        # for result in ans:
        #     print(f"Page Content: {result.page_content}")
        #     print(f"Metadata: {result.metadata}")
        #     print("---")