from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

dataFrame = pd.read_csv("realistic_restaurant_reviews.csv")

embeddings = OllamaEmbeddings(model='mxbai-embed-large')

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if not os.path.exists(db_location):
    os.makedirs(db_location)

if add_documents:
    documents =[]
    ids =[]

    for i, row in dataFrame.iterrows():
        doc = Document(
            page_content=row["Title"]+" "+ row["Review"],
            metadata={"rating": row["Rating"], "date":row["Date"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(doc)

vector_store = Chroma(
    collection_name="realistic_restaurant_reviews.csv",
    persist_directory=db_location,
    embedding_function=embeddings
)
    
if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)

retriever = vector_store.as_retriever(

)
