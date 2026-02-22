# Restaurant Local Agent

A local RAG (Retrieval-Augmented Generation) agent that answers questions about a pizza restaurant using customer reviews. Runs entirely on your machine — no external API calls required.

## How It Works

1. **Ingestion** ([vector.py](vector.py)): Loads restaurant reviews from a CSV file, converts them into vector embeddings using `mxbai-embed-large` (via Ollama), and stores them in a local ChromaDB vector store.
2. **Retrieval**: When a question is asked, relevant reviews are retrieved from the vector store using semantic similarity search.
3. **Generation** ([main.py](main.py)): The retrieved reviews and the question are passed to `llama3.1:8b` (via Ollama) to generate a grounded, context-aware answer.

## Tech Stack

| Component | Tool |
|---|---|
| LLM | Ollama — `llama3.1:8b` |
| Embeddings | Ollama — `mxbai-embed-large` |
| Vector Store | ChromaDB (persisted locally) |
| Orchestration | LangChain |
| Data | Pandas (CSV ingestion) |

## Prerequisites

- [Ollama](https://ollama.com) installed and running locally
- Python 3.9+

Pull the required models before running:

```bash
ollama pull llama3.1:8b
ollama pull mxbai-embed-large
```

## Setup

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

You'll be dropped into an interactive prompt:

```
*************************************
Ask your question (q to quit): What do customers say about the pizza?
```

Type `q` to exit.

> On first run, the vector store is built from [realistic_restaurant_reviews.csv](realistic_restaurant_reviews.csv) and persisted to `./chrome_langchain_db/`. Subsequent runs skip ingestion and load directly from disk.

## Project Structure

```
.
├── main.py                          # Entry point — prompt loop and LLM chain
├── vector.py                        # Embedding, vector store setup, and retriever
├── realistic_restaurant_reviews.csv # Source review data
├── chrome_langchain_db/             # Persisted ChromaDB vector store (auto-generated)
└── requirements.txt
```
