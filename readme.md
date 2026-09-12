# 🚀 DevDocs RAG

> An AI-powered technical documentation assistant built using **Retrieval-Augmented Generation (RAG)** to retrieve relevant documentation and generate accurate, context-grounded answers with source citations.

---

## 📌 Overview

**DevDocs RAG** is a Retrieval-Augmented Generation system designed to help developers interact with technical documentation using natural language.

Instead of relying only on an LLM's pretrained knowledge, the system retrieves relevant information from technical documentation and provides it as context to the language model before generating an answer.

The goal is to build a **production-oriented RAG pipeline** with reliable retrieval, source attribution, and evaluation.

### Example

**Question:**

> How does dependency injection work in FastAPI?

**System:**

1. Understands the query
2. Searches the documentation
3. Retrieves relevant chunks
4. Reranks the retrieved content
5. Provides relevant context to the LLM
6. Generates a grounded answer
7. Returns the relevant source/document information

---

## 🎯 Objectives

* Build an end-to-end RAG pipeline for technical documentation
* Process and index multiple documentation sources
* Generate semantic embeddings for document chunks
* Retrieve relevant documentation using vector search
* Improve retrieval using hybrid search and reranking
* Generate grounded answers using an open/free LLM
* Provide source citations with responses
* Evaluate retrieval and generation quality
* Expose the RAG system through an API
* Containerize the application using Docker

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Query Processing │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Query Rewriting   │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌─────────────────────────────────┐
              │       Hybrid Retrieval          │
              │                                 │
              │   Vector Search + BM25 Search   │
              └────────────────┬────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Reranker       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Relevant Context   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       LLM           │
                    └──────────┬──────────┘
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
              ┌─────────────┐    ┌─────────────┐
              │   Answer    │    │   Sources   │
              └─────────────┘    └─────────────┘
```

---

## 🔄 RAG Pipeline

```text
Technical Documentation
          │
          ▼
   Document Loading
          │
          ▼
    Text Cleaning
          │
          ▼
   Document Chunking
          │
          ▼
     Embeddings
          │
          ▼
     Vector Store
          │
          │
       User Query
          │
          ▼
    Query Processing
          │
          ▼
    Hybrid Retrieval
          │
          ▼
       Reranking
          │
          ▼
   Context Selection
          │
          ▼
         LLM
          │
          ▼
 Answer + Citations
```

---

## ✨ Features

### 📄 Document Processing

* PDF document ingestion
* DOCX document support
* Text extraction
* Text cleaning
* Configurable chunk size
* Configurable chunk overlap
* Document metadata preservation

### 🔎 Retrieval

* Semantic vector search
* Keyword-based retrieval using BM25
* Hybrid retrieval
* Metadata-aware retrieval
* Top-K document retrieval
* Cross-encoder reranking

### 🧠 LLM

* Open/free LLM integration
* Context-grounded generation
* Configurable temperature
* Custom RAG prompts
* Hallucination-aware response generation

### 📚 Source Attribution

Responses include relevant source information such as:

```text
Document: FastAPI Documentation
Page: 24
Section: Dependencies
```

### 📊 Evaluation

The system is designed to evaluate:

* Retrieval accuracy
* Context precision
* Context recall
* Answer relevance
* Faithfulness
* Response latency
* Token usage

### 🌐 API

FastAPI endpoints will provide:

```text
POST /documents/upload
POST /documents/ingest
POST /query
GET  /health
```

---

## 🛠️ Tech Stack

| Component           | Technology                         |
| ------------------- | ---------------------------------- |
| Language            | Python                             |
| RAG Framework       | LangChain                          |
| LLM                 | Groq + Open Model                  |
| Embeddings          | Hugging Face Sentence Transformers |
| Vector Store        | FAISS                              |
| Keyword Search      | BM25                               |
| Reranking           | Cross-Encoder                      |
| Backend             | FastAPI                            |
| Validation          | Pydantic                           |
| Document Processing | PyMuPDF                            |
| Containerization    | Docker                             |
| Testing             | Pytest                             |

---

## 📂 Project Structure

```text
devdocs-rag/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── cleaner.py
│   │   └── chunker.py
│   │
│   ├── embeddings/
│   │   ├── __init__.py
│   │   └── embedding_model.py
│   │
│   ├── vectorstore/
│   │   ├── __init__.py
│   │   └── faiss_store.py
│   │
│   ├── retrieval/
│   │   ├── __init__.py
│   │   ├── retriever.py
│   │   ├── hybrid_search.py
│   │   └── reranker.py
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── prompts.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── pipeline.py
│   │   ├── query_rewriter.py
│   │   └── response.py
│   │
│   └── evaluation/
│       ├── __init__.py
│       ├── evaluator.py
│       └── metrics.py
│
├── data/
│   ├── documents/
│   └── evaluation/
│       └── test_questions.json
│
├── vectorstore/
│
├── scripts/
│   ├── ingest.py
│   └── evaluate.py
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_retrieval.py
│   └── test_rag.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/devdocs-rag.git
cd devdocs-rag
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key

LLM_MODEL=llama-3.3-70b-versatile

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

CHUNK_SIZE=800

CHUNK_OVERLAP=100

VECTOR_DB_PATH=vectorstore/faiss_index
```

### Important

Never commit your `.env` file.

The API key should remain private.

---

## 📚 Adding Documents

Place technical documentation inside:

```text
data/documents/
```

Example:

```text
data/documents/
├── fastapi.pdf
├── langchain.pdf
├── python.pdf
├── docker.pdf
└── postgresql.pdf
```

Then run the ingestion pipeline:

```bash
python scripts/ingest.py
```

The documents will be:

```text
Loaded
  ↓
Cleaned
  ↓
Chunked
  ↓
Embedded
  ↓
Stored in FAISS
```

---

## 💬 Running the RAG System

Start the API:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

---

## 🔍 Example Query

### Request

```json
{
    "question": "How does dependency injection work in FastAPI?"
}
```

### Response

```json
{
    "answer": "FastAPI dependency injection allows reusable...",
    "sources": [
        {
            "document": "fastapi.pdf",
            "page": 24,
            "section": "Dependencies"
        }
    ]
}
```

---

## 📊 Evaluation

A benchmark dataset will be maintained under:

```text
data/evaluation/test_questions.json
```

Example:

```json
[
    {
        "question": "How do FastAPI dependencies work?",
        "expected_source": "fastapi.pdf",
        "expected_answer": "..."
    }
]
```

The evaluation pipeline will measure:

```text
Retrieval
├── Context Precision
├── Context Recall
└── Retrieval Accuracy

Generation
├── Faithfulness
├── Answer Relevance
└── Answer Correctness

Performance
├── Latency
└── Token Usage
```

---

## 🧪 Testing

Run tests using:

```bash
pytest
```

Run a specific test:

```bash
pytest tests/test_retrieval.py
```

---

## 🐳 Docker

Build the image:

```bash
docker build -t devdocs-rag .
```

Run the container:

```bash
docker run -p 8000:8000 devdocs-rag
```

Or use Docker Compose:

```bash
docker-compose up --build
```

---

## 🗺️ Development Roadmap

### Phase 1 — Basic RAG

* [x] Project structure
* [ ] Document loading
* [ ] Text chunking
* [ ] Embeddings
* [ ] FAISS vector store
* [ ] Basic retrieval
* [ ] LLM generation

### Phase 2 — Advanced Retrieval

* [ ] Query rewriting
* [ ] BM25 retrieval
* [ ] Hybrid search
* [ ] Metadata filtering
* [ ] Cross-encoder reranking

### Phase 3 — Answer Quality

* [ ] Source citations
* [ ] Page-level citations
* [ ] Conversation history
* [ ] Context filtering
* [ ] Hallucination prevention
* [ ] "I don't know" handling

### Phase 4 — Evaluation

* [ ] Evaluation dataset
* [ ] Retrieval metrics
* [ ] Generation metrics
* [ ] Latency tracking
* [ ] Token/cost tracking

### Phase 5 — API & Deployment

* [ ] FastAPI
* [ ] API validation
* [ ] Error handling
* [ ] Logging
* [ ] Docker
* [ ] Deployment

### Phase 6 — UI

* [ ] Documentation upload
* [ ] Chat interface
* [ ] Source display
* [ ] Retrieval results
* [ ] Response streaming

---

## 🎯 Future Improvements

* Support Markdown and HTML documentation
* Add documentation versioning
* Add document-level access control
* Add multi-language support
* Add conversational memory
* Add query classification
* Add advanced reranking
* Add streaming responses
* Add observability and tracing
* Add automated evaluation
* Add production vector database support

---

## 💡 Why RAG?

Large Language Models have limitations when working with specialized or frequently updated documentation.

RAG addresses this by retrieving relevant external information before generating an answer.

```text
Traditional LLM

Question
   ↓
LLM
   ↓
Answer
```

RAG:

```text
Question
   ↓
Retriever
   ↓
Relevant Documentation
   ↓
LLM
   ↓
Grounded Answer
```

This helps the system answer questions using the provided documentation rather than relying entirely on the model's pretrained knowledge.

---

## 👨‍💻 Author

**Shivam Singh**

AI Engineer Intern | Generative AI | RAG | LLM Applications

---

## ⭐ Project Status

🚧 **Currently under active development**

The project is being developed incrementally, starting with a basic RAG pipeline and progressing toward hybrid retrieval, reranking, evaluation, API deployment, and a production-oriented architecture.

