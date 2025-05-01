💊 Pharma FAQ Assistant
Pharma FAQ Assistant is an intelligent, NLP-powered question-answering web application built using Python and Streamlit. It allows users to ask free-form queries related to pharmaceutical products and get accurate, relevant responses by semantically searching through a curated FAQ dataset.

🚀 Features
🔍 Semantic Search using Sentence-BERT (intfloat/e5-base-v2)

💡 Query Expansion with Synonyms to improve retrieval accuracy

⚡ FAISS Index for high-speed similarity search

📦 Streamlit UI for interactive user experience

🤖 Trained on a custom Excel-based FAQ dataset

🛠️ Tech Stack
Python

Streamlit – UI framework

SentenceTransformers – For generating embeddings

FAISS – Fast vector similarity search

Pandas – Data loading and manipulation

Pickle – For serializing embedded data

🧠 How It Works
1. Embedding FAQs
Using embed_faqs.py, the application:

Loads FAQs from an Excel file (faqs.xlsx)

Converts each question into an embedding using Sentence-BERT

Saves the embeddings into a FAISS index for fast retrieval

Serializes the question-answer pairs for future lookup

2. Answering User Questions
Using app.py, the app:

Accepts a user's natural language question via the Streamlit UI

Expands the query with relevant synonyms using a pre-defined map

Encodes the expanded query and searches the FAISS index

Returns the most relevant Q&A pair(s) with confidence scores

🧪 Running the Project
🔧 Prerequisites
Make sure you have the following installed:

bash
Copy
Edit
pip install streamlit sentence-transformers faiss-cpu pandas
📁 Files
Ensure these files are present in the project directory:

app.py

embed_faqs.py

faqs.xlsx – Your FAQ dataset

faiss_index.bin – Saved FAISS index

faq_data.pkl – Pickled FAQ question-answer list

▶️ Step 1: Generate Embeddings
bash
Copy
Edit
python embed_faqs.py
▶️ Step 2: Launch Streamlit App
bash
Copy
Edit
streamlit run app.py
📂 FAQ Excel Format
The Excel file (faqs.xlsx) should contain at least the following columns:

Question	Answer
What is Drug X used for?	It is used to treat Condition Y.

🧰 Example Use Cases
Customer support bots for pharma companies

Internal knowledge assistants for healthcare professionals

Quick reference tool for patients and pharmacists

🤝 Contributions
Contributions are welcome! Please open an issue or submit a pull request if you have ideas for improving the assistant — whether that's adding new features, improving search relevance, or UI enhancements.

📜 License
This project is licensed under the MIT License.
