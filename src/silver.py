import pandas as pd
from pathlib import Path
import logging

def run_silver():
    logging.info("Starting Silver Layer")

    bronze_path = Path("bronze/transactions.csv")
    silver_path = Path("silver")
    silver_path.mkdir(exist_ok=True)

    df = pd.read_csv(bronze_path)

    # Standardize columns
    df.columns = df.columns.str.lower().str.strip()

    # Convert date
    df["order_date"] = pd.to_datetime(df["order_date"])

    # Create revenue column
    df["revenue"] = df["quantity"] * df["price"]

    df.to_csv(silver_path / "transactions_cleaned.csv", index=False)

    logging.info("Silver layer completed")