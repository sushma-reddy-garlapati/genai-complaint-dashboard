from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from prometheus_fastapi_instrumentator import Instrumentator
import pickle
import logging
import time
import pandas as pd

# Step 1: Create FastAPI app
app = FastAPI()

# Step 2: Add Prometheus instrumentation
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# Step 3: Setup logging
logging.basicConfig(level=logging.INFO)

# Step 4: Global variables
vectorstore = None
summarizer = None

# Step 5: Pydantic model
class QueryRequest(BaseModel):
    query: str

# Step 6: Load models on startup
@app.on_event("startup")
def load_models():
    global vectorstore, summarizer
    print("🔄 Loading FAISS index and summarizer...")
    vectorstore = pickle.load(open("faiss_index.pkl", "rb"))
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    print("✅ Models loaded.")

# Step 7: Summarization endpoint
@app.post("/summarize")
def summarize_query(request: QueryRequest):
    start = time.time()
    try:
        hits = vectorstore.similarity_search(request.query, k=3)
        combined = " ".join([doc.page_content for doc in hits])
        summary = summarizer(combined, max_length=150, min_length=60, do_sample=False)[0]["summary_text"]
        duration = round(time.time() - start, 2)
        logging.info(f"Query: {request.query} | Duration: {duration}s | Success")
        return {"summary": summary}
    except Exception as e:
        duration = round(time.time() - start, 2)
        logging.error(f"Query failed: {request.query} | Duration: {duration}s | Error: {str(e)}")
        return {"error": "Failed to summarize"}

# Step 8: Complaint lookup
df = pd.read_csv("cleaned_complaints.csv")

@app.get("/complaint/{complaint_id}")
def get_complaint(complaint_id: int):
    match = df[df["Complaint ID"] == complaint_id]
    if not match.empty:
        row = match.iloc[0]
        return {
            "Date received": row["Date received"],
            "Product": row["Product"],
            "Issue": row["Issue"],
            "Company": row["Company"],
            "Narrative": row["cleaned_narrative"]
        }
    else:
        return {"error": f"No complaint found with ID {complaint_id}"}
