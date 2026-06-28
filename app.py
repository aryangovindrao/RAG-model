"""
app.py - Streamlit UI for the RAG pipeline
"""

import os
import streamlit as st

from pipeline import ingest, ask
from vectordb import VECTOR_STORE_PATH

st.set_page_config(page_title="RAG Demo", page_icon="📄")
st.title("📄 RAG Demo - Ask your document")

# --- Sidebar: upload + ingest ---
st.sidebar.header("Upload Document")
uploaded_file = st.sidebar.file_uploader("Choose a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.sidebar.button("Ingest Document"):
        with st.spinner("Processing document..."):
            ingest(file_path)
        st.sidebar.success("Document ingested!")

# --- Main: ask questions ---
st.header("Ask a Question")
question = st.text_input("Your question:")

if st.button("Get Answer"):
    if not os.path.exists(VECTOR_STORE_PATH):
        st.error("No document ingested yet. Upload and ingest one first.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = ask(question)
        st.subheader("Answer")
        st.write(answer)