import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="RetailPulse Dashboard", layout="wide")

st.title("🛍 RetailPulse — Retail Analytics & Loyalty Engine")

gold_path = Path("gold")

# Load Data
kpis = pd.read_csv(gold_path / "kpis.csv")
top_products = pd.read_csv(gold_path / "top_products.csv")
top_customers = pd.read_csv(gold_path / "top_customers.csv")
monthly_sales = pd.read_csv(gold_path / "monthly_sales.csv")
segments = pd.read_csv(gold_path / "customer_segments.csv")

# -----------------------
# KPI Section
# -----------------------
st.header("📊 Key Business Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹ {kpis['total_revenue'][0]:,.0f}")
col2.metric("Total Orders", int(kpis["total_orders"][0]))
col3.metric("Avg Order Value", f"₹ {kpis['average_order_value'][0]:,.0f}")

st.divider()

# -----------------------
# Top Products
# -----------------------
st.subheader("🏆 Top 5 Products by Revenue")
st.bar_chart(top_products.set_index("product"))

# -----------------------
# Top Customers
# -----------------------
st.subheader("💎 Top 5 Customers")
st.bar_chart(top_customers.set_index("customer_name"))

# -----------------------
# Monthly Sales Trend
# -----------------------
st.subheader("📈 Monthly Revenue Trend")
st.line_chart(monthly_sales.set_index("month"))

st.divider()

# -----------------------
# Customer Segments
# -----------------------
st.subheader("🎯 Customer Segmentation")

segment_counts = segments["segment"].value_counts().reset_index()
segment_counts.columns = ["segment", "count"]

st.bar_chart(segment_counts.set_index("segment"))

st.subheader("📋 Detailed Customer Segments")
st.dataframe(segments)

st.divider()

st.write("""
RetailPulse implements an end-to-end retail analytics pipeline using
Bronze-Silver-Gold architecture and RFM-based loyalty segmentation.
""")