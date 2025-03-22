from langchain import LLMMathChain, OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

llm = OpenAI(temperature=0)
chain = LLMMathChain(llm=llm, verbose=True)