import pandas as pd
from pathlib import Path
import logging


def run_loyalty_engine():
    logging.info("Starting Loyalty Engine (RFM)")

    silver_path = Path("silver/transactions_cleaned.csv")
    gold_path = Path("gold")
    gold_path.mkdir(exist_ok=True)

    df = pd.read_csv(silver_path, parse_dates=["order_date"])

    snapshot_date = df["order_date"].max() + pd.Timedelta(days=1)

    # -----------------------
    # RFM Calculation
    # -----------------------

    rfm = df.groupby(["customer_id", "customer_name"]).agg({
        "order_date": lambda x: (snapshot_date - x.max()).days,
        "order_id": "count",
        "revenue": "sum"
    }).reset_index()

    rfm.columns = ["customer_id", "customer_name", "recency", "frequency", "monetary"]

    # -----------------------
    # Scoring (Simple Scaling)
    # -----------------------

    rfm["r_score"] = pd.qcut(rfm["recency"], 4, labels=[4, 3, 2, 1])
    rfm["f_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 4, labels=[1, 2, 3, 4])
    rfm["m_score"] = pd.qcut(rfm["monetary"], 4, labels=[1, 2, 3, 4])

    rfm["rfm_score"] = (
        rfm["r_score"].astype(int) +
        rfm["f_score"].astype(int) +
        rfm["m_score"].astype(int)
    )

    rfm.to_csv(gold_path / "rfm_scores.csv", index=False)

    # -----------------------
    # Customer Segmentation
    # -----------------------

    def segment(score):
        if score >= 10:
            return "Premium"
        elif score >= 7:
            return "Loyal"
        elif score >= 5:
            return "Regular"
        else:
            return "At Risk"

    rfm["segment"] = rfm["rfm_score"].apply(segment)

    rfm.to_csv(gold_path / "customer_segments.csv", index=False)

    logging.info("Loyalty Engine Completed Successfully")