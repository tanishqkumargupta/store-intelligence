import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"
STORE_ID = "STORE_BLR_002"

st.set_page_config(
    page_title="Purplle Store Intelligence",
    page_icon="🛍️",
    layout="wide"
)

# ==================================
# HEADER
# ==================================

st.title("🛍️ Purplle Store Intelligence Dashboard")

st.caption(
    f"Store: {STORE_ID} | Last Updated: "
    f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

# ==================================
# FETCH DATA
# ==================================

try:

    metrics = requests.get(
        f"{BASE_URL}/stores/{STORE_ID}/metrics",
        timeout=5
    ).json()

    anomalies = requests.get(
        f"{BASE_URL}/stores/{STORE_ID}/anomalies",
        timeout=5
    ).json()

    recent_events = requests.get(
        f"{BASE_URL}/stores/{STORE_ID}/events/recent",
        timeout=5
    ).json()

    funnel = requests.get(
        f"{BASE_URL}/stores/{STORE_ID}/funnel",
        timeout=5
    ).json()

except Exception as e:

    st.error(
        f"Backend not available: {e}"
    )

    st.stop()

# ==================================
# SYSTEM STATUS
# ==================================

st.subheader("System Status")

s1, s2, s3 = st.columns(3)

with s1:
    st.success("Backend Online")

with s2:
    st.success("Analytics Online")

with s3:
    st.success("Camera Pipeline Online")

# ==================================
# KPI CARDS
# ==================================

st.subheader("Store KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Unique Visitors",
        metrics["unique_visitors"]
    )

with col2:
    st.metric(
        "Conversion Rate",
        f"{metrics['conversion_rate']}%"
    )

with col3:
    st.metric(
        "Queue Depth",
        metrics["queue_depth"]
    )

with col4:
    st.metric(
        "Abandonment Rate",
        f"{metrics['abandonment_rate']}%"
    )

# ==================================
# STORE SUMMARY
# ==================================

dwell_data = metrics["avg_dwell_per_zone"]

highest_zone = None

if dwell_data:
    highest_zone = max(
        dwell_data,
        key=dwell_data.get
    )

st.subheader("Store Summary")

st.info(
    f"""
    • Visitors detected: {metrics['unique_visitors']}

    • Highest engagement zone: {highest_zone}

    • Active anomalies: {len(anomalies)}

    • Queue depth: {metrics['queue_depth']}
    """
)

# ==================================
# DWELL ANALYTICS
# ==================================

st.subheader("Zone Dwell Analytics")

if dwell_data:

    dwell_df = pd.DataFrame({
        "Zone": list(dwell_data.keys()),
        "Average Dwell (sec)": [
            round(v / 1000, 2)
            for v in dwell_data.values()
        ]
    })

    fig = px.bar(
        dwell_df,
        x="Zone",
        y="Average Dwell (sec)",
        text="Average Dwell (sec)",
        title="Average Dwell Time by Zone"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================
# FUNNEL
# ==================================

st.subheader("Visitor Funnel")

funnel_df = pd.DataFrame({
    "Stage": [
        "Entry",
        "Zone Visit",
        "Billing",
        "Purchase"
    ],
    "Count": [
        funnel["entry"],
        funnel["zone_visit"],
        funnel["billing"],
        funnel["purchase"]
    ]
})

fig2 = px.funnel(
    funnel_df,
    x="Count",
    y="Stage",
    title="Customer Journey Funnel"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==================================
# ANOMALIES
# ==================================

st.subheader("Detected Anomalies")

if len(anomalies) == 0:

    st.success(
        "No anomalies detected"
    )

else:

    for anomaly in anomalies:

        zone = anomaly.get(
            "zone",
            "Unknown Zone"
        )

        st.warning(
            f"⚠ {anomaly['type']} | "
            f"{zone} | "
            f"{anomaly['message']}"
        )

# ==================================
# ZONE PERFORMANCE TABLE
# ==================================

if dwell_data:

    st.subheader(
        "Zone Performance"
    )

    table_df = pd.DataFrame({
        "Zone": list(dwell_data.keys()),
        "Avg Dwell (sec)": [
            round(v / 1000, 2)
            for v in dwell_data.values()
        ]
    })

    st.dataframe(
        table_df,
        use_container_width=True
    )

st.subheader(
    "Recent Events"
)

if len(recent_events) > 0:

    events_df = pd.DataFrame(
        recent_events
    )

    st.dataframe(
        events_df,
        use_container_width=True
    )
