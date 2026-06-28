"""
pipeline.py - Full RAG pipeline (ingestion + question answering)
"""

import os

from loader import load_document
from splitter import split_documents
from embedder import get_embedder
from vectordb import create_vectorstore, load_vectorstore, VECTOR_STORE_PATH
from retriever import retrieve_chunks
from prompt import build_prompt
from llm import generate_answer


def ingest(file_path):
    docs = load_document(file_path)
    chunks = split_documents(docs)
    embedder = get_embedder()
    create_vectorstore(chunks, embedder)
    print(f"Ingested '{file_path}' -> {len(chunks)} chunks stored.")


def ask(question):
    embedder = get_embedder()
    db = load_vectorstore(embedder)
    chunks = retrieve_chunks(db, question)
    prompt = build_prompt(question, chunks)
    answer = generate_answer(prompt)
    return answer


if __name__ == "__main__":
    if not os.path.exists(VECTOR_STORE_PATH):
        ingest("data/HANDBOOK.pdf")

    question = "What is the leave policy?"
    answer = ask(question)
    print("\nQuestion:", question)
    print("Answer:", answer)