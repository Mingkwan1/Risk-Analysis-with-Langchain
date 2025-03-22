from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
from components.load import Load as ld
from components.embedding import Embed as emb
from components.memory import Mem as mem
from components.chain import Chain
import uvicorn

app = FastAPI()

#Intilizing Components

_ = load_dotenv(find_dotenv()) # read local .env file

risk_texts = ld().load()
retriever = emb().emb(risk_texts = risk_texts)
memory = mem().create_mem()

# Initialize the Chain class
qachain = Chain()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        # Call the LLM chain
        result = qachain.Ans_QA(request.query,retriever,memory)
        return {"answer": result["answer"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
