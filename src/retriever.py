def get_retriever(db, k=3):
    return db.as_retriever(search_kwargs={"k": k})

def  retrieve_chunks(db, query, k=3):
    retriever = get_retriever(db, k)
    return retriever.invoke(query)

if __name__ = "__main__":
    from embedder import get_embedder
    from vectordb import load_vectorstore

    embedder = get_embedder()
    db = load_vectorstore(embedder)

    query = "What is 106A. PROMULGATION OF LAWS?"
    results = retrieve_chunks(db, query)

print(f"Top {len(results)} chunks for: '{query}'\n")
for i, chunk in enumerate(results, 1):
    print(f"--- Chunk {i} ---")
    print(chunk.page_content)