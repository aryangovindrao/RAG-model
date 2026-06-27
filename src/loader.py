"""
loader.py - Step 1: Load a document (PDF, DOCX, or TXT)
"""

from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader


def load_document(file_path):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file type")

    return loader.load()


if __name__ == "__main__":
    docs = load_document("data/HANDBOOK.pdf")
    print(f"Loaded {len(docs)} pages")
    print(docs[0].page_content[:200])