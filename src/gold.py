import pandas as pd
from pathlib import Path
import logging


def run_gold():
    logging.info("Starting Gold Layer")

    silver_path = Path("silver/transactions_cleaned.csv")
    gold_path = Path("gold")
    gold_path.mkdir(exist_ok=True)

    df = pd.read_csv(silver_path, parse_dates=["order_date"])

    # -----------------------
    # KPI 1: Total Revenue
    # -----------------------
    total_revenue = df["revenue"].sum()
    total_orders = df["order_id"].nunique()
    avg_order_value = total_revenue / total_orders

    kpi_df = pd.DataFrame({
        "total_revenue": [total_revenue],
        "total_orders": [total_orders],
        "average_order_value": [round(avg_order_value, 2)]
    })

    kpi_df.to_csv(gold_path / "kpis.csv", index=False)

    logging.info(f"Total Revenue: {total_revenue}")
    logging.info(f"Total Orders: {total_orders}")

    # -----------------------
    # Top 5 Products
    # -----------------------
    top_products = (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    top_products.to_csv(gold_path / "top_products.csv", index=False)

    # -----------------------
    # Top 5 Customers
    # -----------------------
    top_customers = (
        df.groupby(["customer_id", "customer_name"])["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    top_customers.to_csv(gold_path / "top_customers.csv", index=False)

    # -----------------------
    # Monthly Sales Trend
    # -----------------------
    df["month"] = df["order_date"].dt.to_period("M")

    monthly_sales = (
        df.groupby("month")["revenue"]
        .sum()
        .reset_index()
    )

    monthly_sales["month"] = monthly_sales["month"].astype(str)

    monthly_sales.to_csv(gold_path / "monthly_sales.csv", index=False)

    logging.info("Gold Layer Completed Successfully")