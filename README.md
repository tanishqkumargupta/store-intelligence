# Purplle Store Intelligence System

## Overview

This project is a computer vision based retail analytics system developed for the Purplle Store Intelligence Challenge.

The system processes CCTV footage, detects and tracks visitors, generates store events, stores analytics data, and exposes intelligence APIs along with a Streamlit dashboard.

---

## Features

### Detection Pipeline

* YOLOv8 person detection
* ByteTrack multi-object tracking
* Zone based visitor analytics
* Entry and exit detection
* Dwell time calculation
* Event generation

### Intelligence APIs

* Event ingestion
* Store metrics
* Funnel analytics
* Anomaly detection
* Health monitoring

### Dashboard

* Visitor KPIs
* Dwell analytics
* Funnel visualization
* Anomaly alerts

---

## Tech Stack

### Computer Vision

* YOLOv8
* ByteTrack
* OpenCV

### Backend

* FastAPI
* SQLAlchemy

### Database

* SQLite

### Dashboard

* Streamlit
* Plotly

---

## System Architecture

CCTV Footage

↓

YOLOv8 Detection

↓

ByteTrack Tracking

↓

Zone Processing

↓

Event Generation

↓

FastAPI Event Ingestion

↓

Database Storage

↓

Analytics APIs

↓

Dashboard

---

## Event Types

### ENTRY

Visitor enters store.

### EXIT

Visitor exits store.

### ZONE_ENTER

Visitor enters a store zone.

### ZONE_DWELL

Visitor spends time within a zone.

---

## API Endpoints

### Event Ingestion

POST /events/ingest

### Metrics

GET /stores/{store_id}/metrics

### Funnel

GET /stores/{store_id}/funnel

### Anomalies

GET /stores/{store_id}/anomalies

### Health

GET /health

---

## Installation

Create virtual environment:

python -m venv .venv

Activate environment:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## Running The Project

### Backend

uvicorn app.main:app --reload

### Detection Pipeline

python pipeline/run_pipeline.py

### Dashboard

streamlit run dashboard/app.py

---

## Data Sources

### CCTV Footage

Store camera footage used for visitor detection and tracking.

### Transaction Data

Brigade_Bangalore.xlsx

Used for retail transaction analytics and conversion calculations.

---

## Store Coverage

### Store 1

Multi-camera retail analytics setup:
- CAM1
- CAM3
- CAM5

### Store 2

Single camera zone analytics setup.

---

## Database Schema

Tables:

- events
- sessions
- transactions
- anomalies

---

## Folder Structure

app/

dashboard/

pipeline/

data/

---

## Known Limitations

* Cross-camera identity matching is not implemented.
* Tracking IDs may change during heavy occlusion.
* Heatmap accuracy depends on manually defined zones.
* Queue analytics is currently a placeholder implementation.

---

## Assumptions

- Zone boundaries are manually configured per store.
- Cameras are treated independently for visitor analytics.
- Transaction data does not contain customer identifiers.
- The system prioritizes reliable event generation over perfect identity persistence.

---

## Future Improvements

* Cross camera identity matching
* Staff identification
* Queue analytics
* Advanced heatmaps
* Real-time deployment

---

## Author

Tanishq Kumar Gupta
