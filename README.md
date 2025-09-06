# 📊 GenAI Complaint Dashboard

A full-stack NLP assistant that retrieves and summarizes consumer complaints using semantic search and LLMs. Built with FastAPI, FAISS, and Hugging Face Transformers, and monitored in real time using Prometheus and Grafana. Includes a modular Streamlit dashboard with hierarchical filtering and clean UI design.

## 💼 Skills Demonstrated

- Python, pandas, regex, NLTK
- FAISS, sentence-transformers, Hugging Face Transformers
- FastAPI, Streamlit
- Prometheus, Grafana
- Git, GitHub, Git LFS
- Modular UI design and observability instrumentation

## 🔗 Live Demo

👉 [Try the Streamlit Dashboard](https://sushma-reddy-garlapati-genai-complaint-dashboard.streamlit.app)


## 🚀 Setup Instructions

```bash
# Start FastAPI backend
uvicorn notebook.rag_api:app --reload

# Launch Streamlit dashboard
streamlit run notebook.app.py

# Start Prometheus
prometheus --config.file=notebook/prometheus.yml

# Start Grafana (macOS example)
brew services start grafana
```
## 🖼️ Screenshots

### 📊 Dashboard Overview  
![Dashboard Overview](images/dashboard_overview.png)

### 🔍 Complaint Explorer  
![Complaint Explorer](images/complaint_explorer.png)

### 🧠 NLP Query Summarizer  
![NLP Query Summarizer](images/nlp_query_summarizer.png)

### 🆔 Complaint ID Lookup  
![Complaint ID Lookup](images/complaint_id_lookup.png)

### 🏦 Company Profile  
![Company Profile](images/company_profile_aes_phea.png)

### 📈 Prometheus Metrics Endpoint  
![Prometheus Metrics](images/prometheus_metrics_endpoint.png)

### 🔎 Prometheus Query Console  
![Prometheus Query Console](images/prometheus_query_console.png)

### 📊 Grafana Request Rate  
![Grafana Request Rate](images/grafana_avg_request_duration.png)

### 📜 FastAPI Swagger Docs  
![FastAPI Swagger Docs](images/fastapi_swagger_docs.png)

