from components.prompt import Prompt as prompt
from components.rag.tools import retrieve as retri_tool

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from langchain_core.messages import SystemMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState

# vectordb = emb().load_cached()
# retriever = retri().CreateRetriever(vectordb)

llm = ChatOpenAI()
state = MessagesState()
systemMessage = prompt()

class Node():

    def __init__(self):
        self.retri_tool = retri_tool
        self.tools = ToolNode([self.retri_tool])

    # Step 1: Generate an AIMessage that may include a tool-call to be sent.
    def query_or_respond(self, state: MessagesState):
        """Generate tool call for retrieval or respond."""
        llm_with_tools = llm.bind_tools([self.retri_tool])
        response = llm_with_tools.invoke(state["messages"])
        # MessagesState appends messages to state instead of overwriting
        # print({"messages": [response], "tools": [self.retri_tool]})
        return {"messages": [response]}

    def execute_tool(self, state: MessagesState):
        # Step 2: Execute the retrieval tool.
        print("HEYYYYY")
        print(state)
        print(state["messages"])
        print("gg",self.tools.invoke(state))
        return self.tools.invoke(state)

    # Step 3: Generate a response using the retrieved content.
    def generate(self, state: MessagesState):
        """Generate answer."""
        # Get generated ToolMessages
        recent_tool_messages = []
        for message in reversed(state["messages"]):
            # print("message:", message)
            if message.type == "tool":
                recent_tool_messages.append(message)
            else:
                break
        tool_messages = recent_tool_messages[::-1]

        # Format into prompt
        docs_content = "\n\n".join(doc.content for doc in tool_messages)
        system_message_content = (
            systemMessage.systemMessage(docs_content) 
        )
        conversation_messages = [
            message
            for message in state["messages"]
            if message.type in ("human", "system")
            or (message.type == "ai" and not message.tool_calls)
        ]
        prompt = [SystemMessage(system_message_content)] + conversation_messages

        # Run
        response = llm.invoke(prompt)
        return {"messages": [response]}





# def retrieve(state: State):
#     retrieved_docs = retriever.invoke(state["question"])
#     # retrieved_docs = vectordb.similarity_search(state["question"])
#     return {"context": retrieved_docs}
# @tool(response_format="content_and_artifact")
# def retrieve(query: str):
#     """Retrieve information related to a query."""
#     retrieved_docs = retriever.invoke(query, k=2)
#     serialized = "\n\n".join(
#         (f"Source: {doc.metadata}\n" f"Content: {doc.page_content}")
#         for doc in retrieved_docs
#     )
#     return serialized, retrieved_docs

# def generate(state: State):
#     docs_content = "\n\n".join(doc.page_content for doc in state["context"])
#     messages = prompt.invoke({"question": state["question"], "context": docs_content})
#     print("messages:", messages)
#     llm=ChatOpenAI()
#     response = llm.invoke(messages)
#     return {"answer": response.content}
