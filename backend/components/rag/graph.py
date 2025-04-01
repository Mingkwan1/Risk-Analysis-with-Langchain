from langgraph.graph import START, StateGraph
from IPython.display import Image, display
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState, StateGraph

from components.rag.nodes import Node
from langgraph.prebuilt import ToolNode
from components.rag.tools import retrieve as retri_tool


from langgraph.graph import END
from langgraph.prebuilt import tools_condition

import time
from pathlib import Path

state = MessagesState()

class Graph():
    def __init__(self):
        # self.memory = MemorySaver()
        # self.graph_builder = StateGraph(State).add_sequence([retrieve, generate])
        # self.graph_builder.add_edge(START, "retrieve")
        # self.graph = self.graph_builder.compile(
        #     # checkpointer=self.memory
        #     )
        # query_or_respond = nodes().query_or_respond()
        # tools = nodes().tools()
        # generate = nodes().generate()
        self.nodes = Node()
        self.retri_tool = retri_tool
        self.tools = ToolNode([self.retri_tool])
        self.memory = MemorySaver()
        self.config = {"configurable": {"thread_id": "abc123"}}

        self.graph_builder = StateGraph(MessagesState)
        self.graph_builder.add_node("query",self.nodes.query_or_respond)
        self.graph_builder.add_node("tools",self.tools)
        self.graph_builder.add_node("generate",self.nodes.generate)

        self.graph_builder.set_entry_point("query")
        self.graph_builder.add_conditional_edges(
            "query",
            tools_condition,
            {END: END, "tools": "tools"},
        )
        self.graph_builder.add_edge("tools", "generate")
        self.graph_builder.add_edge("generate", END)

        self.graph = self.graph_builder.compile(
            checkpointer=self.memory
        )

    def show(self):
        mermaid_png = self.graph.get_graph().draw_mermaid_png()
        Path("workflow.png").write_bytes(mermaid_png)
        # display(Image("workflow_png"))

    def generate(self, query):
        start_time = time.time()
        self.config = {"configurable": {"thread_id": "1"}}
        result = self.graph.invoke({"question": query}
                                #    , self.config
                                   )
        # print(f'Context: {result["context"]}\n\n')
        # print("---------------------------------------------------")
        print(f'Answer: {result["answer"]}')
        print(f"Generating in {time.time()-start_time:.2f}s")
        return result
    
    def stream(self, query):
        start_time = time.time()
        # for step in self.graph.stream(
        #     {"question": query}
        #     , stream_mode="updates"):

        for step in self.graph.stream(
            {"messages": [{"role": "user", "content": query}]
            #  , "tools": [self.retri_tool]
             },
            stream_mode="values",
            config = self.config,
        ):
            step["messages"][-1].pretty_print()
        
        print(f"{step}\n\n----------------\n")
        print(f"Finsihed streaming in {time.time()-start_time:.2f}s")
