#use ollama directly into code using OllamaLLM package from langchain ollama library, 
# essentially running Ollama in background and exposing to our python code via http/api
from langchain_ollama.llms import OllamaLLM 
#
from langchain_core.prompts import ChatPromptTemplate

from vector import retriever

model = OllamaLLM(model="llama3.1:8b")

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews :  {reviews}

Here is the question you need to answer : {question} 
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n*************************************")
    question = input("Ask you question (q to quit)")
    print("\n\n")
    if(question=="q"):
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews":reviews,"question":question})
    print(result)




