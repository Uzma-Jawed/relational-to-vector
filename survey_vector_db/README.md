# Survey Vector Search (Relational DB → Embeddings → Vector Search)

This project demonstrates an **end-to-end AI pipeline** that converts **relational survey data** into **semantic embeddings** and performs **vector-based similarity search**.

The goal is to show how structured databases (questions, answers, scores, binary values) can be transformed into vectors for modern AI use cases like semantic search.

---

## 🔹 Project Flow

```
SQLite (Relational DB)
  → Questions & Answers
  → Semantic Text Creation
  → Embeddings (Sentence Transformers)
  → Vector Index (FAISS)
  → Semantic Search Results + Metadata
```

---

## 📁 Project Structure

```
survey_vector_db/
│
├── data/
│   ├── survey.db              # Relational database (SQLite)
│   └── faiss/
│       ├── survey.index       # FAISS vector index
│       └── metadata.pkl       # Metadata (binary, score, question_id)
│
├── scripts/
│   ├── create_db.py           # Create relational tables
│   ├── insert_data.py         # Insert sample questions & answers
│   ├── embed_and_store.py     # Generate embeddings & store in FAISS
│   ├── query_vectors.py       # Semantic search on vectors
│   └── check_data.py          # Verify relational data
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create & activate virtual environment

```bash
python -m venv milvus
milvus\Scripts\activate   # Windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run (Step-by-Step)

### Step 1: Create relational database

```bash
python scripts/create_db.py
```

### Step 2: Insert sample data

```bash
python scripts/insert_data.py
```

### Step 3: Verify relational data

```bash
python scripts/check_data.py
```

### Step 4: Generate embeddings & store vectors (FAISS)

```bash
python scripts/embed_and_store.py
```

### Step 5: Perform semantic search

```bash
python scripts/query_vectors.py
```

---

## 🔍 Example Query

```python
query = "employee motivation and job satisfaction"
```

The system retrieves **semantically similar survey answers** along with:

* `question_id`
* `binary` value (Yes/No, True/False)
* `score`

---

## 🧠 Key Concepts Demonstrated

* Relational database design (SQLite)
* Question–Answer normalization
* Text embeddings using Sentence Transformers
* Vector indexing using FAISS
* Semantic similarity search
* Metadata preservation alongside vectors

---

## ✅ Notes

* Only **semantic fields (question + answer text)** are embedded.
* Binary values and scores are stored as **metadata**, not vectors.
* FAISS is used for local vector search due to Windows compatibility.

---

## 👩‍💻 Author

Built as part of an **AI Internship learning task** to understand how to convert structured databases into vector-based semantic search systems.