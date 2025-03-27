from langgraph.graph import START, StateGraph
from IPython.display import Image, display

from components.rag.state import State
from components.rag.nodes import retrieve, generate

import time
from pathlib import Path

class Graph():
    def __init__(self):
        self.graph_builder = StateGraph(State).add_sequence([retrieve, generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()

    def show(self):
        mermaid_png = self.graph.get_graph().draw_mermaid_png()
        Path("workflow.png").write_bytes(mermaid_png)
        # display(Image("workflow_png"))

    def generate(self, query):
        start_time = time.time()
        result = self.graph.invoke({"question": query})
        # print(f'Context: {result["context"]}\n\n')
        # print("---------------------------------------------------")
        print(f'Answer: {result["answer"]}')
        print(f"Generating in {time.time()-start_time:.2f}s")
        return result
    def stream(self, query):
        start_time = time.time()
        for step in self.graph.stream(
            {"question": query}
            , stream_mode="updates"):
            print(f"{step}\n\n----------------\n")
        print(f"Finsihed streaming in {time.time()-start_time:.2f}s")