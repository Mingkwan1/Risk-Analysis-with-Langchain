from langchain.memory import ConversationBufferMemory

class Mem:
    def __init__(self):
        pass
    def create_mem(self):
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
            )
        return memory
