import streamlit as st
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# ------------------------------
# 🔁 Synonym Expansion Logic
# ------------------------------
SYNONYM_MAP = {
    "strength": ["dosage", "dose", "concentration", "potency", "mg", "milligram", "formulation"],
    "indication": ["use", "purpose", "prescribed for", "treatment", "condition"],
    "dispose": ["discard", "throw away", "get rid of", "eliminate", "safely remove"],
    "adverse": ["side effects", "reactions", "harmful effects", "complications"],
    "overdose": ["excess intake", "too much", "overuse", "accidental high dose"],
    "storage": ["keep", "store", "preserve", "conditions", "temperature"],
    "available": ["present", "existing", "in stock", "existing strength", "strength"],
    "reaction": ["effect", "response", "reaction", "side effect"],
    "drug": ["medicine", "med", "compound", "product"],
    "capsule": ["pill", "tablet", "dose", "form"]
}

def expand_query_with_synonyms(query: str, synonym_map: dict) -> str:
    expanded_query = query
    query_lower = query.lower()
    
    for key_term, synonyms in synonym_map.items():
        if key_term in query_lower:
            for synonym in synonyms:
                expanded_query += f" {synonym}"
    
    return expanded_query

# ------------------------------
# 📦 Load model and data
# ------------------------------
model = SentenceTransformer('intfloat/e5-base-v2')
index = faiss.read_index("faiss_index.bin")

with open('faq_data.pkl', 'rb') as f:
    faq_data = pickle.load(f)

# ------------------------------
# 💬 Streamlit UI
# ------------------------------
st.title("Pharma FAQ Assistant")
st.markdown("Ask a question, and we'll find the most relevant answer from our database.")

user_query = st.text_input("Your question:", placeholder="e.g., Can I take Drug X with alcohol?")

if user_query:
    # 🔁 Expand query with synonyms
    expanded_query = expand_query_with_synonyms(user_query, SYNONYM_MAP)

    # 🧠 Embed and search
    query_embedding = model.encode([f"query: {expanded_query}"], normalize_embeddings=True)
    scores, indices = index.search(np.array(query_embedding).astype('float32'), k=3)

    top_idx = indices[0][0]
    top_score = scores[0][0]

    if top_score > 0.5:
        st.subheader("Best Match:")
        st.markdown(f"**Q:** {faq_data[top_idx]['Question']}")
        st.markdown(f"**A:** {faq_data[top_idx]['Answer']}")
        st.markdown(f"_Confidence: {top_score:.2f}_")

        # ↩ Alternatives
        with st.expander("Not what you're looking for? See other relevant responses"):
            for i in range(1, 3):
                idx = indices[0][i]
                score = scores[0][i]
                if score > 0.5:
                    st.markdown(f"**Q:** {faq_data[idx]['Question']}")
                    st.markdown(f"**A:** {faq_data[idx]['Answer']}")
                    st.markdown(f"_Confidence: {score:.2f}_")
                    st.markdown("---")
    else:
        st.warning("Sorry, we couldn't find a relevant answer. Please try rephrasing your question.")
