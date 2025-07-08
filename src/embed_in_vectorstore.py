import chromadb

def embed_in_vectorstore(df, embeddings):
    #Embed the preprocessed narrative in a vector store.
    
    client = chromadb.PersistentClient(path="../data/vector_store")

    try:
        collection = client.get_collection(name="complaint_narrative")
    except:
        collection = client.create_collection(name="complaint_narrative" ,  metadata={"narrative" :"A collection of complaint narratives"})
    
    print("Collection created.")
    ids = [f"narrative_{i}" for i in range(len(df))]
    documents = df["preprocessed_narrative"].tolist()
    metadatas = []
    
    for _, row in df.iterrows():
        metadatas.append({
            'complaint_id': row['Complaint ID'],
            'product': row['Product'],
            'sub_product': row['Sub-product'],
            'issue': row['Issue'],
            'sub_issue': row['Sub-issue'],
            'company': row['Company'],
            'state': row['State'],
            'zip_code': row['ZIP code'],
            'date_received': row['Date received'],
            'submitted_via': row['Submitted via'],
            'consumer_consent': row['Consumer consent provided?'],
            'tags': row['Tags'],
            'timely_response': row['Timely response?'],
            'company_response': row['Company response to consumer']
        })
    batch_size = 5000  
    try:
        embeddings = embeddings.tolist() 
    except:
        pass
    num_batches = len(df) // batch_size + 1
    
    for i in range(num_batches):
        start = i * batch_size
        end = min((i + 1) * batch_size, len(df))
    
        batch_embeddings = embeddings[start:end]
        batch_documents = documents[start:end]
        batch_metadatas = metadatas[start:end]
        batch_ids = ids[start:end]
    
        collection.add(
            embeddings=batch_embeddings,
            documents=batch_documents,
            metadatas=batch_metadatas,
            ids=batch_ids
        )
    
        print(f"Added batch {i + 1}/{num_batches}")
    
    print(f"Added {len(df)} documents to the collection.")\
    
    return collection