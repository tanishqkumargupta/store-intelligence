from sqlalchemy import (
    Column,
    String,
    Float,
    Boolean,
    Integer,
    DateTime,
    JSON
)

from app.database import Base


class Event(Base):
    __tablename__ = "events"

    event_id = Column(String, primary_key=True)
    store_id = Column(String)
    camera_id = Column(String)
    visitor_id = Column(String)

    event_type = Column(String)

    timestamp = Column(DateTime)

    zone_id = Column(String, nullable=True)

    dwell_ms = Column(Integer)

    is_staff = Column(Boolean)

    confidence = Column(Float)

    metadata_json = Column(JSON)


class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(String, primary_key=True)

    visitor_id = Column(String)

    store_id = Column(String)

    entry_time = Column(DateTime)

    exit_time = Column(DateTime, nullable=True)

    converted = Column(Boolean, default=False)

    purchase_count = Column(Integer, default=0)


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(String, primary_key=True)

    invoice_number = Column(String)

    store_id = Column(String)

    store_name = Column(String)

    brand_name = Column(String)

    product_name = Column(String)

    salesperson_name = Column(String)

    quantity = Column(Integer)

    total_amount = Column(Float)

    timestamp = Column(DateTime)


class Anomaly(Base):
    __tablename__ = "anomalies"

    anomaly_id = Column(String, primary_key=True)

    store_id = Column(String)

    anomaly_type = Column(String)

    severity = Column(String)

    detected_at = Column(DateTime)

    suggested_action = Column(String)
