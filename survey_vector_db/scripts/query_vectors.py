import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("data/faiss/survey.index")

# Load metadata
with open("data/faiss/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# -------------------------
# User query
# -------------------------
query = "employee motivation and job satisfaction"

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

# -------------------------
# Search in FAISS
# -------------------------
k = 3  # top results
distances, indices = index.search(query_embedding, k)

# -------------------------
# Show results
# -------------------------
print("\n🔍 Query:", query)
print("\n📊 Top Results:\n")

for rank, idx in enumerate(indices[0]):
    print(f"Result {rank+1}")
    print("Distance:", distances[0][rank])
    print("Metadata:", metadata[idx])
    print("-" * 40)