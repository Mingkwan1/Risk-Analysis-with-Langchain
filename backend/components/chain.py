from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from components.prompt import Prompt as prm
from components.embedding import Embed as emb

class Chain:
    def __init__(self):
        pass
    def CreateChain(self, risk_text, retriever, memory):
        retriever=emb().emb(risk_text)
        qa = ConversationalRetrievalChain.from_llm(
            llm = ChatOpenAI(temperature = 0),
            retriever=retriever,
            memory=memory,
        )
        return qa
    def Ans_QA(self, risk_text, query, retriever, memory):
        chain = self.CreateChain(risk_text, retriever, memory)
        prompt = prm().CreatePrompt()
        formatted_prompt = prompt.format(question = query)
        result = chain.invoke({"question": formatted_prompt})
        print(result["answer"])
        return result
    

