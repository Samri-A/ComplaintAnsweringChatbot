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
    try:
           """Run a query using the Openrouter model api."""
           embeddings = HuggingFaceEmbeddings(
             model_name="sentence-transformers/all-MiniLM-L6-v2",
             model_kwargs={'device': 'cpu'}
              )
           vector_store = Chroma(persist_directory="../data/vector_store", embedding_function=embeddings)
           retriever = vector_store.as_retriever()
           docs = retriever.invoke(prompt)
           context = "\n\n".join([ f"[Source: {doc.metadata.get('source', 'unknown')}, Page: {doc.metadata.get('page', 'N/A')}]\n{doc.page_content}"
             for doc in docs])
           
             
           response = client.chat.completions.create(
             model="openrouter/cypher-alpha:free",
             messages=[
               {
                     "role": "system",
                     "content": """"
                     You are a financial services assistant chatbot trained to analyze and respond to customer complaints based on real historical data. You have access to a knowledge base containing customer complaint narratives submitted to the Consumer Financial Protection Bureau (CFPB). Your goal is to provide accurate, compliant, and helpful answers using the retrieved complaint data.
         
                     Use the retrieved complaint documents to:
                     
                     Understand the customer's issue
                     
                     Identify relevant product, sub-product, and issue types
                     
                     Provide helpful, brief, and professional responses based on how similar complaints were handled
                     
                     Always respond in a formal tone, and include any helpful information that aligns with past complaint resolutions. If the query cannot be answered from the retrieved documents, clearly state:
                     “The provided documents do not contain enough information to accurately respond to your query.”
                      Always cite source text chunks from the documents provided. Do not guess or hallucinate.
                      Please provide your response in the following format:
         
                      Answer:
                      <your detailed answer here>
                      
                      Sources:
                      - Source: <source1>, 
                      - Source: <source2>, 
                      """ 
                    
                    
         
                 },
               {
                 "role": "user",
                 "content": 
                 f"""
                 Question:
                  {prompt}
                  
                  Documents:
                  {context}
                  
                  Please provide a complete answer with proper citations from the provided documents.
                  """
               }
               
             ],
             stream = False
           )
           return response.choices[0].message.content
    except Exception as e:
          return f"Error ocurred{str(e)}"

