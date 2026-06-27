from langchain.ollama import OllamaLLM

def get_llm(model="llama3"):
    return OllamaLLM(model=model)

def generate_answer(prompt, model="llama3"):
    llm = get_llm(model)
    return llm.invoke(prompt)


if __name__ == "__main__":
    from embedder import get_embedder
    from vectordb import load_vectorstore
    from retriever import retrieve_chunks
    from prompt import build_prompt
 
    embedder = get_embedder()
    db = load_vectorstore(embedder)
 
    question = "What is 106A. PROMULGATION OF LAWS?"
    chunks = retrieve_chunks(db, question)
    prompt = build_prompt(question, chunks)
 
    answer = generate_answer(prompt)
    print("Answer:", answer)