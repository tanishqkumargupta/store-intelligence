from fastapi import FastAPI
from app.database import engine
from app.models import Base, Transaction
from typing import List
from app.routes.metrics import router as metrics_router
from app.routes.funnel import router as funnel_router
from app.routes.events import (
    router as events_router
)
from app.routes.anomalies import (
    router as anomalies_router
)
from app.routes.transactions import (
    router as transaction_router
)
from fastapi import Depends
from sqlalchemy.orm import Session
from app.routes.heatmap import (
    router as heatmap_router
)
from app.schemas import EventCreate
from app.dependencies import get_db
from app.ingestion import (
    event_exists,
    create_event
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Store Intelligence API",
    version="1.0"
)

app.include_router(metrics_router)
app.include_router(
    anomalies_router
)
app.include_router(
    heatmap_router
)
app.include_router(funnel_router)
app.include_router(transaction_router)
app.include_router(
    events_router
)


@app.get("/")
def root():
    return {
        "message": "Store Intelligence API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/events/ingest")
def ingest_events(
    events: List[EventCreate],
    db: Session = Depends(get_db)
):
    success = []
    duplicates = []

    for event in events:

        existing = event_exists(
            db,
            event.event_id
        )

        if existing:
            duplicates.append(event.event_id)
            continue

        create_event(db, event)

        success.append(event.event_id)

    return {
        "ingested": len(success),
        "duplicates": len(duplicates),
        "success_ids": success,
        "duplicate_ids": duplicates
    }


@app.get("/transactions/count")
def count_transactions(
        db: Session = Depends(get_db)
):
    return {
        "count": db.query(
            Transaction
        ).count()
    }
