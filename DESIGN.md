# DESIGN DOCUMENT

## 1. Problem Statement

The objective is to convert raw CCTV footage into actionable retail intelligence by detecting visitors, tracking movement, measuring dwell time, generating events, and exposing analytics through APIs and dashboards.

---

## 2. System Architecture

The solution follows a modular event-driven architecture.

CCTV Video

↓

YOLOv8 Person Detection

↓

ByteTrack Multi-Object Tracking

↓

Zone Mapping

↓

Event Generation

↓

FastAPI Ingestion

↓

Database Storage

↓

Analytics Services

↓

Dashboard

---

## 3. Detection Layer

### YOLOv8

YOLOv8 is used to detect people in each frame.

Reasons:

* Fast inference speed
* Lightweight deployment
* Good retail CCTV performance
* Easy integration with Python

Output:

* Bounding boxes
* Confidence scores

---

## 4. Tracking Layer

### ByteTrack

ByteTrack is used to assign identities to detected visitors.

Responsibilities:

* Track visitors across frames
* Maintain visitor IDs
* Reduce duplicate detections

Challenges:

* Occlusions
* Partial visibility
* Crowded scenes

Known limitation:

Long occlusions may cause ID reassignment.

---

## 5. Zone Analytics Layer

Each store area is represented using manually defined polygon zones.

Examples:

* BACK_WALL
* PROMO_ISLAND
* MAKEUP_TABLE
* IQ_COUNTER

The visitor foot point is used for zone determination.

Reason:

The foot point represents the actual physical location of the visitor more accurately than the box center.

---

## 6. Event Generation Layer

Events are generated whenever visitor state changes.

Target Event Types:

### ENTRY

Generated when a visitor crosses the entry line.

### EXIT

Generated when a visitor exits the store.

### ZONE_ENTER

Generated when a visitor enters a new zone.

### ZONE_DWELL

Generated when a visitor leaves a zone after spending time there.

---

## 7. Backend Layer

FastAPI is used as the central service.

Responsibilities:

* Event ingestion
* Metrics computation
* Funnel analytics
* Anomaly detection
* Health monitoring

Reasons:

* High performance
* Easy API development
* Automatic documentation

---

## 8. Database Design

The system stores:

### Events

Raw event stream generated from CCTV.

### Sessions

Visitor lifecycle information.

### Transactions

Purchase and POS information.

### Anomalies

Detected operational issues.

---

## 9. Analytics Layer

### Metrics

* Unique visitors
* Average dwell time
* Queue depth
* Conversion rate

### Funnel

Entry

↓

Zone Visit

↓

Billing

↓

Purchase

### Anomalies

Examples:

* High dwell time
* Low conversion
* Queue spikes

---

## 10. Dashboard

Streamlit is used for visualization.

Displayed Insights:

* Store KPIs
* Funnel analytics
* Dwell analytics
* Operational anomalies

---

## 11. Scalability

Future improvements include:

* Multi-camera fusion
* Staff identification
* Cross-camera re-identification
* Real-time deployment
* Advanced heatmaps

## 12. AI-Assisted Decisions

AI tools were used during development to accelerate implementation, debugging, documentation, and architectural exploration.

Areas where AI assistance was used:

* Reviewing FastAPI project structure and API organization.
* Evaluating tracking approaches such as ByteTrack and DeepSORT.
* Debugging event generation and database integration issues.
* Refining documentation including README, DESIGN, and CHOICES documents.
* Reviewing implementation tradeoffs and identifying limitations.

All architectural decisions, implementation choices, testing, and final validation were performed by the developer.
