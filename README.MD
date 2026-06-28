# RAG Demo

A simple Retrieval-Augmented Generation (RAG) pipeline for asking questions
about your own documents (PDF, DOCX, TXT) using local embeddings and a
local LLM (Ollama).

## Architecture

```
PDF/DOCX/TXT → loader.py → splitter.py → embedder.py → vectordb.py (FAISS)
                                                              │
User Question → retriever.py → prompt.py → llm.py (Ollama) → Answer
```

## Project Structure

```
rag-demo/
├── data/                  # source documents
├── embeddings/
│   └── vector_store/      # saved FAISS index
├── loader.py               # load PDF/DOCX/TXT
├── splitter.py             # chunk documents
├── embedder.py              # embedding model
├── vectordb.py              # FAISS store/load
├── retriever.py             # similarity search
├── prompt.py                # build prompt
├── llm.py                  # call Ollama LLM
├── pipeline.py               # wires everything together
├── app.py                  # Streamlit UI
├── requirements.txt
└── README.md
```

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install and run [Ollama](https://ollama.com), then pull the model:
   ```
   ollama pull llama3
   ```

3. Place your document(s) in the `data/` folder.

## Usage

### CLI

```
python pipeline.py
```

This ingests `data/HANDBOOK.pdf` (first run only) and answers a sample
question.

### Web UI

```
streamlit run app.py
```

Upload a document in the sidebar, click **Ingest Document**, then ask
questions in the main panel.

## How It Works

1. **Load** — Extract raw text from the document.
2. **Split** — Break text into overlapping chunks.
3. **Embed** — Convert each chunk into a vector (sentence-transformers).
4. **Store** — Save vectors in a FAISS index.
5. **Retrieve** — On a question, embed the query and find the top-K similar chunks.
6. **Prompt** — Combine the question and retrieved chunks into a prompt.
7. **Generate** — Send the prompt to the LLM (Ollama) and return the answer.

## Future Enhancements

- Hybrid search (BM25 + vector)
- Reranking with cross-encoders
- Source citations (page/chunk references)
- Conversation memory
- Evaluation with RAGAS