# ARCHITECTURAL CHOICES & TRADEOFFS

## Overview

This document explains the major design decisions taken during development and the tradeoffs considered.

---

# 1. Why YOLOv8?

### Alternatives Considered

* Faster R-CNN
* YOLOv5
* YOLOv8

### Decision

YOLOv8 was selected because it provides a strong balance between:

* Detection accuracy
* Inference speed
* Ease of deployment

### Tradeoff

A larger model could improve detection quality but would reduce processing speed on commodity hardware.

---

# 2. Why ByteTrack?

### Alternatives Considered

* DeepSORT
* OC-SORT
* ByteTrack

### Decision

ByteTrack was selected because it is lightweight, easy to integrate, and performs well in retail environments.

### Tradeoff

Long occlusions may result in ID reassignment.

This was accepted in favor of maintaining real-time performance.

---

# 3. Why Zone-Based Analytics?

### Decision

The solution uses predefined polygon zones instead of attempting full store mapping.

Reasons:

* Simpler deployment
* Easy customization
* Works across different store layouts

### Tradeoff

Zone definitions require manual calibration per store.

---

# 4. Why Foot Point Based Localization?

### Decision

The bottom center point of the bounding box is used for zone assignment.

### Reason

The foot position better represents the actual physical location of a visitor than the box center.

### Benefit

Reduces incorrect zone assignments for tall bounding boxes.

---

# 5. Why FastAPI?

### Decision

FastAPI was selected for all backend APIs.

### Benefits

* High performance
* Automatic Swagger documentation
* Strong typing with Pydantic
* Easy deployment

---

# 6. Why Streamlit?

### Decision

Streamlit was used for rapid dashboard development.

### Benefits

* Fast prototyping
* Interactive charts
* Minimal frontend code

### Tradeoff

Not intended for large-scale production dashboards.

---

# 7. Why Event-Driven Architecture?

### Decision

The system converts video observations into events.

Examples:

* ENTRY
* EXIT
* ZONE_ENTER
* ZONE_DWELL

### Benefits

* Easier analytics
* Historical replay
* Scalable API design

---

# 8. Why Single-Camera Analytics Per Zone?

### Decision

Each camera is treated as the primary source for zones visible within its field of view.

### Reason

The provided CCTV streams are not synchronized and do not contain camera calibration information.

### Tradeoff

Cross-camera identity matching was intentionally excluded from the final implementation.

---

# 9. Handling Detection Uncertainty

Retail CCTV environments introduce:

* Occlusions
* Partial visibility
* Crowded scenes
* Overlapping visitors

The system uses:

* Confidence filtering
* Tracking persistence
* Zone transition cooldowns

to reduce false event generation.

---

# 10. Known Limitations

* Visitor IDs may change after long occlusions.
* Cross-camera re-identification is not implemented.
* Zone boundaries require manual configuration.
* Queue analytics are dependent on camera placement.
* Session-to-purchase correlation is currently simplified due to the absence of customer identifiers in transaction data.

---

# 11. Future Improvements

* Multi-camera fusion
* Person re-identification
* Staff recognition
* Automated zone generation
* Real-time cloud deployment
