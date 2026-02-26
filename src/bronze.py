import pandas as pd
from pathlib import Path
import logging

def run_bronze():
    logging.info("Starting Bronze Layer")

    data_path = Path("retailpulse/data/transactions.csv")
    bronze_path = Path("bronze")
    bronze_path.mkdir(exist_ok=True)

    df = pd.read_csv(data_path)
    df.to_csv(bronze_path / "transactions.csv", index=False)

    logging.info("Bronze layer completed")