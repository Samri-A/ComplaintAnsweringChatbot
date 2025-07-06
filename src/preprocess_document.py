import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
 

def preprocess_document(df):
    
    #Preprocess the document by splitting text into chunks and encoding them.
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=256,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    
    narrative_chunks = text_splitter.split_text(df["preprocessed_narrative"].tolist())
    
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    embeddings = model.encode(narrative_chunks)
    
    return embeddings.tolist()