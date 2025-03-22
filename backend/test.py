import os

path = "C:/Users/(Ming)MingkwanRattan/OneDrive - STelligence Co., Ltd/Play/Langchain/JuiceCompany/backend/data"
if not os.path.exists(path):
    print(f"The directory does not exist: {path}")
else:
    print(f"The directory exists: {path}")