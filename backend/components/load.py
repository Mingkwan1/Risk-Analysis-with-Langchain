from langchain.schema import Document
import os, json

class Load:
    def __init__(self):
        pass
    def load(self):
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
                    #print(data)

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
        return risk_texts
