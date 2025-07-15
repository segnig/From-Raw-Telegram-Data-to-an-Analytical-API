# 📊 From Raw Telegram Data to Analytical API | Kara Solutions

## 🧠 Overview

This project builds a robust **Data Engineering Pipeline** for extracting and analyzing health product-related data from public **Ethiopian medical Telegram channels**. Developed at **Kara Solutions**, the goal is to uncover insights that help stakeholders track trends in medical products, vendor activity, pricing, and visual content through object detection.

The pipeline spans **ETL/ELT architecture**, data modeling, enrichment via **YOLOv8**, and serving analytics via **FastAPI**, orchestrated end-to-end using **Dagster**.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Business Questions](#-business-questions)
- [Project Architecture](#-project-architecture)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [API Usage](#-api-usage)
- [Database Schema](#-database-schema)
- [Learnings](#-learnings)
- [Deliverables](#-deliverables)
- [Author](#-author)
- [License](#-license)

---

## ❓ Business Questions

The platform answers:

1. 💊 What are the **top 10 most frequently mentioned** medical products or drugs?
2. 🏷 How do **prices or availability** of products vary across different Telegram channels?
3. 🖼 Which channels have the most **visual content** (e.g., images of pills, creams)?
4. 📆 What are the **daily/weekly trends** in health-related message volume?

---

## 🏗 Project Architecture

```mermaid
flowchart TD
    A[Telegram Channels] -->|Telethon Scraper| B[Raw JSON Files]
    B --> C[PostgreSQL: Raw Tables]
    C -->|dbt Transformations| D[Staging + Fact/Dim Tables]
    B --> E[YOLOv8 Image Classifier]
    E --> D
    D -->|Query Engine| F[FastAPI Server]
    F -->|API| G[Business Reports/UI]
    all -->|Dagster Jobs| Scheduler
````

---

## 🧰 Technologies Used

| Category                | Stack / Tools                 |
| ----------------------- | ----------------------------- |
| Telegram Scraping       | Telethon                      |
| Data Storage            | PostgreSQL                    |
| Data Modeling           | dbt                           |
| Object Detection        | YOLOv8 (Ultralytics)          |
| API Development         | FastAPI, Uvicorn              |
| Orchestration           | Dagster                       |
| Containerization        | Docker, Docker Compose        |
| Secrets Management      | python-dotenv                 |
| Documentation & Testing | dbt Docs, dbt Tests, Pydantic |

---

## 🗂 Project Structure

```bash
.
├── data/
│   ├── raw/                      # JSON files: raw telegram messages
│   └── images/                   # Scraped image files for YOLO
├── dagster_pipeline/            # Dagster job & op definitions
├── dbt_project/                 # dbt models, seeds, docs, tests
├── fastapi_app/
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   └── crud.py
├── Dockerfile                   # Docker image for FastAPI
├── docker-compose.yml           # PostgreSQL + FastAPI + Dagster
├── .env                         # Secrets & config
├── requirements.txt             # Python packages
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. 🔐 Environment Setup

Create a `.env` file:

```env
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
DB_HOST=postgres
DB_PORT=5432
DB_NAME=telegram_data
DB_USER=postgres
DB_PASSWORD=your_password
```

> ❗ Note: Add `.env` to `.gitignore`

---

### 2. 🐳 Docker + Postgres Setup

```bash
docker-compose up --build
```

### 3. 🔗 DBT Initialization

```bash
cd dbt_project
dbt init
dbt build
dbt docs generate
```

---

### 4. 🚀 Run Dagster UI

```bash
dagster dev
```

Dagster UI: [http://localhost:3000](http://localhost:3000)

---

## 📡 API Usage (via FastAPI)

Start the API:

```bash
uvicorn fastapi_app.main:app --reload
```

### 🔎 Endpoints

| Endpoint                                 | Description                                 |
| ---------------------------------------- | ------------------------------------------- |
| `/api/reports/top-products?limit=10`     | Top N frequently mentioned medical products |
| `/api/channels/{channel_name}/activity`  | Posting activity for a channel              |
| `/api/search/messages?query=paracetamol` | Search for messages containing a keyword    |

Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧱 Database Schema

### ⭐ Star Schema

* **dim\_channels**
  `channel_id`, `channel_name`, `category`, `scraped_date`

* **dim\_dates**
  `date_id`, `year`, `month`, `week`, `weekday`

* **fct\_messages**
  `message_id`, `channel_id`, `date_id`, `message_text`, `has_image`, `word_count`

* **fct\_image\_detections**
  `message_id`, `object_class`, `confidence_score`


---

## 📘 Learnings

* ✅ Modular dbt models make transformation logic maintainable
* 🧠 Using YOLOv8 to enrich structured data with visual insights was effective
* ⚙️ Dagster's UI and job orchestration made debugging and scheduling intuitive
* 🔐 Managing secrets with `.env` and containerization guarantees reproducibility

---

## 📤 Deliverables

* ✅ Full DAG of the data pipeline in Dagster
* ✅ dbt project with:

  * Raw → Staging → Marts model layers
  * Documentation and tests
* ✅ FastAPI endpoints answering business questions
* ✅ YOLOv8 image enrichment logic
* ✅ Dockerized, reproducible environment
* ✅ GitHub repository
* ✅ Report + diagrams

---

## 👨‍💻 Author

**Segni Girma**
🌍 Adama, Ethiopia
📫 Email: \[[segnigirma11@gmail.com](mailto:segnigirma11@gmail.com)]
🔗 LinkedIn: [linkedin.com/in/validresults](https://linkedin.com/in/validresults)

---

## 🪪 License

This project is licensed under the [MIT License](./LICENSE).

```