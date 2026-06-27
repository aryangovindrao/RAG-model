"""
vectordb.py - Step 4: Store and load the FAISS vector database
"""

from langchain_community.vectorstores import FAISS

VECTOR_STORE_PATH = "embeddings/vector_store"


def create_vectorstore(chunks, embedder):
    db = FAISS.from_documents(chunks, embedder)
    db.save_local(VECTOR_STORE_PATH)
    return db


def load_vectorstore(embedder):
    return FAISS.load_local(
        VECTOR_STORE_PATH,
        embedder,
        allow_dangerous_deserialization=True,
    )


if __name__ == "__main__":
    from loader import load_document
    from splitter import split_documents
    from embedder import get_embedder

    docs = load_document("data/HANDBOOK.pdf")
    chunks = split_documents(docs)
    embedder = get_embedder()

    db = create_vectorstore(chunks, embedder)
    print(f"Saved vector store to '{VECTOR_STORE_PATH}' with {len(chunks)} chunks")