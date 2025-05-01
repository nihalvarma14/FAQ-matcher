import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Load model
model = SentenceTransformer('intfloat/e5-base-v2')  # Or use MiniLM for smaller model

# Load FAQ Excel
df = pd.read_excel('faqs.xlsx')

# Preprocess questions (prompt format for E5)
faq_questions = [f"passage: {q}" for q in df['Question'].tolist()]
faq_embeddings = model.encode(faq_questions, normalize_embeddings=True)

# Save index
dim = faq_embeddings.shape[1]
index = faiss.IndexFlatIP(dim)
index.add(np.array(faq_embeddings).astype('float32'))
faiss.write_index(index, 'faiss_index.bin')

# Save questions & answers for later retrieval
with open('faq_data.pkl', 'wb') as f:
    pickle.dump(df.to_dict(orient='records'), f)

print("FAISS index and data saved.")
