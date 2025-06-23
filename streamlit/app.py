import asyncio
import streamlit as st
import pandas as pd
from pinotdb import connect
from datetime import datetime
import time
import plotly.express as px
import os
import requests

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# ------------------------------------------------------------------------
# Pinot connection
# ------------------------------------------------------------------------
pinot_host = os.environ.get("PINOT_SERVER", "pinot-broker")
pinot_port = int(os.environ.get("PINOT_PORT", 8099))
conn = connect(pinot_host, pinot_port)

delivery_service_api = "http://localhost:8888"

# ------------------------------------------------------------------------
# Page layout
# ------------------------------------------------------------------------
st.set_page_config(layout="wide")
st.title("Chewy Real‑Time Dashboard 🐾")

now = datetime.now()
st.write(f"Last update: {now:%d %B %Y %H:%M:%S}")

# ------------------------------------------------------------------------
# Auto‑refresh controls
# ------------------------------------------------------------------------
if "sleep_time" not in st.session_state:
    st.session_state.sleep_time = 6
if "auto_refresh" not in st.session_state:
    st.session_state.auto_refresh = True

auto_refresh = st.checkbox("Auto refresh?", st.session_state.auto_refresh)
if auto_refresh:
    st.session_state.sleep_time = st.number_input(
        "Refresh rate (sec)", value=st.session_state.sleep_time, step=1
    )

# ------------------------------------------------------------------------
# Back‑end availability check
# ------------------------------------------------------------------------
curs = conn.cursor()
pinot_available = False
try:
    curs.execute('SELECT * FROM orders WHERE "timestamp" > ago(\'PT2M\')')
    pinot_available = curs.description is not None
    if pinot_available and not list(curs):
        st.warning("Connected to Pinot broker but no recent orders.", icon="⚠️")
except Exception as e:
    st.warning(
        f"Unable to connect to Apache Pinot at {pinot_host}:{pinot_port}\n\n{e}",
        icon="⚠️",
    )

# ------------------------------------------------------------------------
# Main dashboard
# ------------------------------------------------------------------------
if pinot_available:

    # KPI OVERVIEW ------------------------------------------------------
    response = requests.get(f"{delivery_service_api}/orders/overview").json()
    current_time_period  = response["currentTimePeriod"]
    previous_time_period = response["previousTimePeriod"]

    def delta(curr, prev): return None if prev is None else f"{curr - prev:,}"

    col1, col2, col3 = st.columns(3)
    col1.metric("# Orders",        f"{current_time_period['orders']:,}",
                delta(current_time_period["orders"], previous_time_period["orders"]))
    col2.metric("Total ₹",         f"{current_time_period['totalPrice']:,}",
                delta(current_time_period["totalPrice"], previous_time_period["totalPrice"]))
    col3.metric("Avg Order ₹",     f"{current_time_period['avgOrderValue']:.2f}",
                delta(round(current_time_period["avgOrderValue"], 2),
                      round(previous_time_period["avgOrderValue"], 2)))

    col4, col5, col6 = st.columns(3)
    col4.metric("Fraud",           f"{current_time_period['fraudCount']:,}",
                delta(current_time_period["fraudCount"], previous_time_period["fraudCount"]))
    col5.metric("Delivered",       f"{current_time_period['deliveredCount']:,}",
                delta(current_time_period["deliveredCount"], previous_time_period["deliveredCount"]))
    col6.metric("Refunded",        f"{current_time_period['refundedCount']:,}",
                delta(current_time_period["refundedCount"], previous_time_period["refundedCount"]))

    # Fraud / Delivered / Refunded BAR -------------------------------
    st.subheader("Current vs. Previous • Fraud / Delivered / Refunded")
    bar_df = pd.DataFrame({
        "Type":     ["Fraud", "Delivered", "Refunded"],
        "Current":  [current_time_period["fraudCount"],
                     current_time_period["deliveredCount"],
                     current_time_period["refundedCount"]],
        "Previous": [previous_time_period["fraudCount"],
                     previous_time_period["deliveredCount"],
                     previous_time_period["refundedCount"]],
    }).melt(id_vars="Type", var_name="Period", value_name="Count")
    st.plotly_chart(px.bar(bar_df, x="Type", y="Count", color="Period",
                           barmode="group"), use_container_width=True)

    # ORDERS‑PER‑MINUTE ----------------------------------------------
    raw = requests.get(f"{delivery_service_api}/orders/ordersperminute").json()

    if isinstance(raw, dict):
        raw = [raw]

    ts_df = pd.DataFrame(raw)

    st.subheader("Orders per Minute – raw")
    st.dataframe(ts_df.head())

    if len(ts_df) > 1:
        melt = ts_df.melt(id_vars="timestamp",
                          value_vars=["orders", "revenue", "fraud",
                                      "delivered", "refunded"],
                          var_name="metric", value_name="value")
        for metr in ["orders", "fraud", "revenue", "delivered", "refunded"]:
            series = melt[melt.metric == metr]
            st.plotly_chart(px.line(series, x="timestamp", y="value",
                                    title=metr.capitalize()),
                            use_container_width=True)


    # LATEST ORDERS ----------------------------------------------------
    st.subheader("Latest Orders")
    latest_df = pd.DataFrame(
        requests.get(f"{delivery_service_api}/orders/latestorders").json()
    )
    st.dataframe(latest_df)


    # TOP 5 Popular Categories & Items ---------------------------------
    popular_raw = requests.get(f"{delivery_service_api}/orders/popular").json()

    # Categories -------------------------------------------------------
    st.subheader("Top 5 Popular Categories")
    cat_df = pd.DataFrame(popular_raw.get("categories", []))
    if not cat_df.empty:
        st.dataframe(cat_df)
        cat_long = cat_df.melt(id_vars="category",
                               value_vars=["orders", "quantity"],
                               var_name="Metric", value_name="Count")
        st.plotly_chart(
            px.bar(cat_long, x="category", y="Count", color="Metric",
                   barmode="group", title="Top Categories – Orders vs. Quantity"),
            use_container_width=True
        )

    # Items ------------------------------------------------------------
    st.subheader("Top 5 Popular Items")
    item_df = pd.DataFrame(popular_raw.get("itemNames", []))
    if not item_df.empty:
        st.dataframe(item_df)
        item_long = item_df.melt(id_vars="itemName",
                                 value_vars=["orders", "quantity"],
                                 var_name="Metric", value_name="Count")
        st.plotly_chart(
            px.bar(item_long, x="itemName", y="Count", color="Metric",
                   barmode="group", title="Top Items – Orders vs. Quantity"),
            use_container_width=True
        ) 

    curs.close()

# ------------------------------------------------------------------------
# Auto‑refresh trigger
# ------------------------------------------------------------------------
if auto_refresh:
    time.sleep(st.session_state.sleep_time)
    st.rerun()
