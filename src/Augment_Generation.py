from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from openai import OpenAI
import os
load_dotenv()


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= os.getenv("token"),  
)


def run_query(prompt):
  """Run a query using the OpenAI client."""
  embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
     )
  vector_store = Chroma(persist_directory="../data/vector_store", embedding_function=embeddings)
  retriever = vector_store.as_retriever()
  docs = retriever.invoke(prompt)
  context = "\n".join([doc.page_content for doc in docs])
    
    
  response = client.chat.completions.create(
    model="openrouter/cypher-alpha:free",
    messages=[
      {
            "role": "system",
            "content": "You are a financial analyst assistant for CrediTrust. Your task is to answer questions about customer complaints. Use the following retrieved complaint excerpts to formulate your answer. If the context doesn't contain the answer, state that you don't have enough information.:\n" + context
        },
      {
        "role": "user",
        "content": prompt
      }
      
    ],
    stream = False
  )
  return response.choices[0].message.content

