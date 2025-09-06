# 📊 GenAI Complaint Dashboard

A full-stack NLP assistant that retrieves and summarizes consumer complaints using semantic search and LLMs. Built with FastAPI, FAISS, and Hugging Face Transformers, and monitored in real time using Prometheus and Grafana. Includes a modular Streamlit dashboard with hierarchical filtering and clean UI design.

---

## 🌟 Project Highlights

- 🔍 **Semantic Search**: Retrieve relevant complaints using FAISS and sentence-transformers
- 🧠 **LLM Summarization**: Generate concise summaries with Hugging Face Transformers
- 📊 **Interactive Dashboard**: Filter complaints by state, company, and ID with Streamlit
- 📈 **Real-Time Monitoring**: Prometheus metrics and Grafana dashboards for observability
- 🧪 **Modular Architecture**: Clean separation of backend, frontend, and monitoring layers
- ☁️ **Cloud-Ready**: Dropbox integration for large CSVs, FastAPI designed for Render/Railway deployment

---

## 💼 Skills Demonstrated

- Python, pandas, regex, NLTK
- FAISS, sentence-transformers, Hugging Face Transformers
- FastAPI, Streamlit
- Prometheus, Grafana
- Git, GitHub, Git LFS
- Modular UI design and observability instrumentation
- Cloud deployment troubleshooting and API integration

---

## 🔗 Live Demo

👉 [Try the Streamlit Dashboard](https://sushma-reddy-garlapati-genai-complaint-dashboard.streamlit.app)

---

## 🧰 Tech Stack

**Backend**: FastAPI, FAISS, Hugging Face Transformers  
**Frontend**: Streamlit  
**Monitoring**: Prometheus, Grafana  
**Data**: Consumer complaint dataset (CSV via Dropbox)  
**Deployment**: Streamlit Cloud (frontend), local backend (cloud-ready)

---

## 🚀 Setup Instructions

### 🔧 Backend (FastAPI)

```bash
# Install dependencies
pip install -r requirements.txt

# Start FastAPI backend
uvicorn notebook.rag_api:app --host 0.0.0.0 --port 8000 --reload
```

### 🖥️ Frontend (Streamlit)

```bash
# Launch Streamlit dashboard
streamlit run notebook/app.py
```

### 📊 Monitoring (Prometheus + Grafana)

```bash
# Start Prometheus
prometheus --config.file=notebook/prometheus.yml

# Start Grafana (macOS example)
brew services start grafana
```

> Note: Prometheus scrapes metrics from FastAPI at `/metrics`. Grafana visualizes request rate, latency, and system health.

---

## 📊 Monitoring & Observability

This project includes full-stack observability:

- Metrics exposed via `/metrics` using `prometheus_fastapi_instrumentator`
- Prometheus queries track request rate, latency, and uptime
- Grafana dashboards visualize system health over time
- Includes PromQL queries for:
  - `http_requests_total`
  - `faas_request_duration_seconds_sum`
  - `gc_objects_collected_total`
  - `rate(faas_requests_total{faas_function=~".*"}[1m])`
  - `sum(rate(faas_requests_total[1m])) by (function)`

---

## 🖼️ Screenshots

### 📊 Dashboard Overview  
![Dashboard Overview](images/dashboard_overview.png)

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

---

## 🔮 Future Improvements

- 🌐 Deploy FastAPI backend to Render or Railway for full cloud integration
- 🔐 Add authentication for complaint lookup and summarization
- 📦 Package as a pip-installable module for reuse
- 📄 Add unit tests and CI/CD pipeline
- 🧠 Integrate RAG pipeline with vector search and streaming summarization
- 📊 Add Grafana alerting and uptime dashboards

---

## 📁 Repository

👉 [GitHub: genai-complaint-dashboard](https://github.com/sushma-reddy-garlapati/genai-complaint-dashboard)

---

## 🧑‍💻 Author

**Sushma Reddy Garlapati**  
Aspiring NLP Engineer | Backend Developer | Open-source Contributor  
Focused on building recruiter-ready GenAI demos with real-time observability and clean UI design.

📫 Contact: [LinkedIn](https://www.linkedin.com/in/sushma-reddy-garlapati) | [GitHub](https://github.com/sushma-reddy-garlapati)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

---

Let me know when you’re ready to add badges, a walkthrough GIF, or a short video demo. You’ve built something robust and presented it like a product engineer with open-source instincts. This README will absolutely stand out.
```
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

