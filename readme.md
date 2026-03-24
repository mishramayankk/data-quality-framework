# Data Quality & Validation Framework (Snowflake ↔ Elasticsearch)

## Overview

A **config-driven data validation framework** that compares datasets between Snowflake and Elasticsearch to ensure data consistency, reliability, and pipeline health.

The system performs automated checks (e.g., row counts), retries failed operations, and sends alerts on mismatches.

---

## Features

* Config-driven validation (no hardcoding)
* Snowflake ↔ Elasticsearch data comparison
* Retry with exponential backoff
* Slack alerting for failures
* Modular and extensible design

---

## Architecture

```
            +------------------+
            |   Config Files   |
            +------------------+
                     |
                     v
            +------------------+
            |   Python Engine  |
            | (Validation Job) |
            +------------------+
              |              |
              v              v
      +-------------+   +-------------+
      | Snowflake   |   | Elasticsearch|
      +-------------+   +-------------+
              \              /
               \            /
                v          v
             +----------------+
             | Validation     |
             | + Alerting     |
             +----------------+
```

---

## Project Structure

```
data-quality-framework/
│── config/
│   ├── config.json        # Credentials & connections
│   ├── rules.json         # Validation rules
│
│── src/
│   ├── snowflake_client.py
│   ├── elastic_client.py
│   ├── validator.py
│   ├── alert.py
│   ├── retry.py
│
│── jobs/
│   ├── run_pipeline.py    # Main execution script
│
│── requirements.txt
│── README.md
```

---

## Setup

### 1. Clone Repository

```bash
git clone <repo-url>
cd data-quality-framework
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

### `config/config.json`

```json
{
  "snowflake": {
    "user": "",
    "password": "",
    "account": "",
    "warehouse": "",
    "database": "",
    "schema": ""
  },
  "elasticsearch": {
    "host": "http://localhost:9200"
  },
  "slack_webhook": ""
}
```

---

### `config/rules.json`

```json
{
  "tables": [
    {
      "name": "patients",
      "snowflake_query": "SELECT COUNT(*) FROM patients",
      "es_index": "patients_index",
      "checks": ["count_match"]
    }
  ]
}
```

---

## Running the Pipeline

```bash
python jobs/run_pipeline.py
```

---

## Sample Output

```
patients: {'status': True, 'sf_count': 1000, 'es_count': 1000}
claims: {'status': False, 'sf_count': 1200, 'es_count': 1180}
```

---

## Alerting

* On mismatch, a Slack alert is triggered:

```
Data Mismatch Detected:
[{'table': 'claims', 'sf_count': 1200, 'es_count': 1180}]
```

---

## Extending the Framework

### Add New Validation

Update `validator.py`:

```python
def null_check(...):
    pass
```

Then reference in `rules.json`:

```json
"checks": ["count_match", "null_check"]
```

---

### Add New Table

Just update config:

```json
{
  "name": "new_table",
  "snowflake_query": "...",
  "es_index": "...",
  "checks": ["count_match"]
}
```

---

## Production Improvements (Recommended)

* Add logging (structured logs)
* Integrate Airflow for scheduling
* Store historical results for anomaly detection
* Add parallel execution (ThreadPool / multiprocessing)
* Dockerize for deployment
* CI/CD via GitHub Actions

---

## Tech Stack

* Python
* Snowflake
* Elasticsearch
* REST APIs (Slack Webhooks)

---

## Use Cases

* Data pipeline validation
* Cross-system consistency checks
* Monitoring ingestion pipelines
* Detecting data drift or loss

---

## Resume Impact

* Demonstrates **end-to-end data engineering ownership**
* Highlights **data quality, reliability, and monitoring**
* Shows **real-world system design + automation**

---

## Future Enhancements

* Column-level validation
* Schema drift detection
* Z-score anomaly detection
* Web dashboard for reports

---

## Author

Mayank Mishra
