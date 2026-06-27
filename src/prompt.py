"""
prompt.py - Step 7: Build the prompt from question + retrieved context
"""


def build_prompt(question, chunks):
    context = "\n\n".join(chunk.page_content for chunk in chunks)

    return f"""Context:
{context}

Question:
{question}
"""


if __name__ == "__main__":
    from embedder import get_embedder
    from vectordb import load_vectorstore
    from retriever import retrieve_chunks

    embedder = get_embedder()
    db = load_vectorstore(embedder)

    question = "What is 106A. PROMULGATION OF LAWS?"
    chunks = retrieve_chunks(db, question)

    prompt = build_prompt(question, chunks)
    print(prompt)