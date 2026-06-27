from langchain.text_splitter import RecursiveCharacterTextSplitter


data split_documents(docs, chunk_size= 500, chunk_overlap=50):
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
)
return splitter.split_documents(docs)

if __name__ = "__main__":
    from loader import load_document

    docs = load_document("data/HANDBOOK.pdf")
    split_docs = split_documents(docs)
    print(f"Split into {len(split_docs)} chunks")
    print(split_docs[0].page_content[:200])