# 📊 Ethiopian Medical Data Platform — Kara Solutions

## 🧠 Business Need

As a Data Engineer at **Kara Solutions**, your mission is to design a robust and scalable data platform that generates actionable insights from **public Telegram channels** related to **Ethiopian medical businesses**.

By building an end-to-end data pipeline, this platform aims to answer key business questions:

* 🔟 What are the **top 10 most frequently mentioned** medical products or drugs?
* 📉 How does the **price or availability** of a product vary across channels?
* 🖼️ Which channels share the most **visual content** (e.g., pills, creams)?
* 📆 What are the **daily and weekly trends** in posting volume?

This solution leverages a **modern ELT architecture** to extract Telegram data, clean and transform it using `dbt`, enrich it using `YOLOv8` object detection on images, and finally serve insights through a FastAPI-based analytical API.

---

## 🧱 Project Architecture

```
Raw Telegram Data (JSON + Images)
                ↓
            Data Lake
                ↓
PostgreSQL Data Warehouse (via loader scripts)
                ↓
   dbt (Staging → Marts in Star Schema)
                ↓
    YOLOv8 Image Object Detection
                ↓
      Analytical API (FastAPI)
                ↓
        Business Intelligence
```

---

## 🚀 Key Technologies

| Component        | Tool/Framework       | Purpose                                     |
| ---------------- | -------------------- | ------------------------------------------- |
| Data Extraction  | Telethon             | Scrape public Telegram messages and media   |
| Data Storage     | Local JSON/Image     | Store raw structured and unstructured data  |
| Data Warehouse   | PostgreSQL           | Central repository for transformed data     |
| Transformation   | dbt                  | Build staging and mart models (star schema) |
| Enrichment       | YOLOv8 (Ultralytics) | Detect objects in medical-related images    |
| API Layer        | FastAPI              | Expose insights via analytical endpoints    |
| Orchestration    | Dagster              | Schedule and monitor data pipeline jobs     |
| Containerization | Docker               | Reproducible environment and services       |

---

## 🧩 Data Model Design

The project follows a **dimensional modeling** approach:

* **Fact Tables**:

  * `fct_messages`: One row per Telegram message with keys and metrics.
  * `fct_image_detections`: One row per object detection result (linked to `fct_messages`).
* **Dimension Tables**:

  * `dim_channels`: Metadata about Telegram channels.
  * `dim_dates`: Calendar dimension for temporal aggregation.

---

## ✅ Project Setup Tasks (Task 0)

* 🐳 Containerized PostgreSQL & Python using Docker.
* 🔐 `.env` file for secret management (Telegram API, DB creds).
* 📦 `requirements.txt` for reproducible dependency setup.
* 📁 Modular project folder structure with clear separation of concerns.

---

## 📥 Task 1 — Data Scraping & Loading

* Scrape data using Telethon from:

  * [Chemed](https://t.me/lobelia4cosmetics)
  * [Tikvah Pharma](https://t.me/tikvahpharma)
* Organize raw data in:
  `data/raw/telegram_messages/YYYY-MM-DD/channel_name.json`
* Collect and store media images for YOLO processing.
* Log errors and channel status for monitoring.

---

## 🔄 Task 2 — Data Modeling & Transformation

* Load raw JSON into PostgreSQL under the `raw` schema.
* Initialize `dbt` and create:

  * `staging` models to clean and structure the raw data.
  * `mart` models to implement star schema (facts + dimensions).
* Implement built-in and custom tests:

  * `not_null`, `unique`, and semantic data rules.
* Auto-generate documentation with `dbt docs`.

---

## 🧠 Task 3 — Data Enrichment with YOLOv8

* Use `ultralytics` YOLOv8 to detect objects (e.g., bottles, boxes) in message images.
* Parse and structure detections into a `fct_image_detections` table:

  ```sql
  Columns:
  - message_id (FK to fct_messages)
  - detected_class
  - confidence_score
  ```
* Link visual data to textual insights.

---

## 🌐 Task 4 — FastAPI Analytical API

Expose insights via RESTful endpoints:

* `/api/reports/top-products`: Top mentioned products.
* `/api/channels/{channel}/activity`: Posting activity by channel.
* `/api/search/messages?query=...`: Keyword search across messages.

Use Pydantic for data validation and schema consistency.

---

## ⏱️ Task 5 — Pipeline Orchestration (Dagster)

* Use `Dagster` to define ops and jobs for:

  * `scrape_telegram_data`
  * `load_raw_to_postgres`
  * `run_dbt_transformations`
  * `run_yolo_enrichment`
* Launch with `dagster dev` for visual monitoring.
* Add daily or hourly scheduling as needed.

---

## 📚 Learning Outcomes

* ELT pipeline design & implementation.
* Advanced data modeling with `dbt`.
* Integration of structured and unstructured data.
* API development and pipeline orchestration.
* Real-world production practices (testing, logging, secrets management).

---

## 📅 Timeline & Milestones

| Task     | Status         | Deadline                |
| -------- | -------------- | ----------------------- |
| Task 0–2 | ✅ Completed    | July 12, 2025 (Interim) |
| Task 3–5 | 🔄 In Progress | July 15, 2025 (Final)   |

---

## 👨‍🏫 Mentors

* Mahlet
* Rediet
* Kerod
* Rehmet

---

## 📌 Notes

* All credentials are managed securely via `.env`.
* This project is reproducible using Docker and follows IaC principles.
* Refer to the `/docs` directory or `dbt docs serve` for full documentation.

---

## 📂 Repository Structure (Example)

```
├── data/
│   ├── raw/
│   └── processed/
├── dbt/
│   └── kara_dbt_project/
├── scripts/
│   ├── scrape.py
│   ├── detect_objects.py
│   └── run_pipeline.sh
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── crud.py
├── dagster_pipeline/
│   ├── jobs.py
│   └── ops.py
├── Dockerfile
├── docker-compose.yml
├── .env
└── requirements.txt
```