import os

data_dir = r"C:/Users/(Ming)MingkwanRattan/OneDrive - STelligence Co., Ltd/Play/Langchain/JuiceCompany/backend/data"
risk_texts = []
for file_name in os.listdir(data_dir):
    if file_name.endswith(".json"):
        file_path = os.path.join(data_dir, file_name)
        print(file_path)