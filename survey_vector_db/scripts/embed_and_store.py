import sqlite3
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import os

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read relational data
conn = sqlite3.connect("data/survey.db")
cursor = conn.cursor()

cursor.execute("""
SELECT q.id, q.question_text, a.answer_text, a.binary_value, a.score
FROM questions q
JOIN answers a ON q.id = a.question_id
""")

rows = cursor.fetchall()
conn.close()

texts = []
metadata = []

for r in rows:
    text = f"Question: {r[1]} Answer: {r[2]}"
    texts.append(text)
    metadata.append({
        "question_id": r[0],
        "binary": r[3],
        "score": r[4]
    })

# Generate embeddings
embeddings = model.encode(texts)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# Save index & metadata
os.makedirs("data/faiss", exist_ok=True)
faiss.write_index(index, "data/faiss/survey.index")

with open("data/faiss/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("✅ Step 6 complete: Embeddings stored using FAISS")