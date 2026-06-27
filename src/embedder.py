from langchain.huggingface import HuggingFaceEmbeddings

def get_embeddder():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


if __name__ == "__main__":
    embeddder = get_embedder();
    vector = embedder.embed_query("What is the  106A. PROMULGATION OF LAWS")
    print(f"Embedding length: {len(vector)}")
    print(vector[:5])