from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveJsonSplitter
import time

import os, json

class Load:
    def __init__(self):
        pass
    
    def load(self):
        start_time = time.time()  # Start timer
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        
        risk_texts = []

        for file_name in os.listdir(data_dir):
            if file_name.endswith(".json"):
                file_path = os.path.join(data_dir, file_name)

        # Extract year, topic, and part from the file name
                file_parts = file_name.split(".")[0].split("_")  # Split into [year, topic, part]
                # print(file_parts) Checking the loaded file
                year = file_parts[0]  # Extract year
                company = file_parts[1]  # Extract topic
                part = file_parts[2] if len(file_parts) > 2 else "1"  # Extract part if it exists
        # File is encoded in utf-16
                ##Checking the endocing of the files##
                # with open(file_path, "rb") as file:
                #     raw_data = file.read()
                #     result = chardet.detect(raw_data)
                #     encoding = result["encoding"]
                #     print("Detected encoding:", encoding)

                # with open(file_path, "r", encoding=encoding) as file:
                #     data = json.load(file)

                with open(file_path, 'r', encoding='utf-16') as file:
                    data = json.load(file)
                    # print(data)

                # 1.4) Initialize a list to store the collected data

                    # Traverse the JSON structure
                    for item in data["Report"]:  # Iterate through the list 
                        if "Risk Category" in item:  # Check if "Risk Category" exists
                            for sub_item in item["Risk Category"]:  # Iterate through the list
                                # Extract Category, Risk_Detail, and Risk_Topic
                                Category = sub_item.get("Category")
                                Risk_Detail = sub_item.get("Risk Detail")
                                Risk_Topic = sub_item.get("Risk Topic")

                                # Create a unique identifier for the data
                                page_content = f"Category: {Category}, Risk_Detail: {Risk_Detail}, Risk_Topic: {Risk_Topic}"

                                metadata = {
                                            "year": year,
                                            "company": company,
                                            "part": part,
                                            "Category": Category,
                                            "Risk_Detail": Risk_Detail,
                                            "Risk_Topic": Risk_Topic
                                        }
                                # Append the data to the list
                                doc = Document(
                                            page_content=page_content,
                                            metadata=metadata
                                        )
                                risk_texts.append(doc)
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"Loading completed in {elapsed_time:.2f} seconds")
        return risk_texts
    
    def load_json(self):
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        risk_texts = []

        for file_name in os.listdir(data_dir):
            # if file_name.endswith(".json"):
            #     file_path = os.path.join(data_dir, file_name)
            #     with open(file_path, 'r', encoding='utf-16') as file:
            #         data = json.load(file)
            #         # print(data)
            #         risk_texts.append(data)
                # with open("combined.json", "w") as f:
                #     json.dump(risk_texts, f, indent=4)
            with open("combined.json", 'r') as file:
                risk_texts = json.load(file)
        return(risk_texts)


class Split():
    def __init__(self):
        pass
    def jsonsplit(self, risk_texts):
        JSONsplitter = RecursiveJsonSplitter(max_chunk_size=300)
        docs = JSONsplitter.create_documents(risk_texts)
        print(docs[0])
        print("----------------")
        print(docs[1])
        print("----------------")
        print([doc for doc in docs][:10], "...")
        print("----------------")
        return(docs)
    
    def Rsplit(self, risk_texts):
        start_time = time.time()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=40,
            length_function=len,
            is_separator_regex=False,
        )
        texts = text_splitter.split_documents(risk_texts)
        # print(type(risk_texts))
        # print(texts[0])
        # print(texts[1])
        # print(len(texts))
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"Splitting completed in {elapsed_time:.2f} seconds")
        return(texts)