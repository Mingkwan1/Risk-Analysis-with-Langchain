from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import time, os

### 2.) Vector storing and Embedding ###

#2021_CFRESH file is in window1252
#2023 KBS have an error char, iNCOMPLETE BLACKET and no report year at the end

class Embed:
    def __init__(self):
        self.embedding = OpenAIEmbeddings()
        self.persist_directory = 'docs/chroma/'
    def emb(self, risk_texts):
        start_time = time.time()
        #Save to statics

        ###Chroma vectordb
        vectordb = Chroma.from_documents(documents = risk_texts,
                                  persist_directory=self.persist_directory, 
                                  embedding=self.embedding)
        
        ## Can be change to FAISS for small and Pinecone for large
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"Embedding completed in {elapsed_time:.2f} seconds")
        return vectordb
    
    def load_cached(self):
        """Load pre-computed embeddings (fast)"""
        if os.path.exists(self.persist_directory):
            start = time.time()
            self.vectordb = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embedding
            )
            print(f"Loaded cached embeddings in {time.time()-start:.2f}s")
            return self.vectordb
        else:
            raise FileNotFoundError("No cached embeddings found. Run embed_and_save() first")
