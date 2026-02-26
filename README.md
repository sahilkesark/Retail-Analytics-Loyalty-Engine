🛍 RetailPulse — Retail Analytics & Loyalty Engine
📌 Overview

RetailPulse is an end-to-end retail analytics system that transforms raw transaction data into business-ready insights using a structured Bronze–Silver–Gold ETL architecture and an RFM-based Loyalty Engine.

The system enables retailers to monitor revenue performance, identify top customers and products, and segment customers for strategic decision-making.

🏗 Architecture
Raw Data → Bronze → Silver → Gold → Dashboard
🔹 Bronze Layer

Ingests raw transaction data

Stores unmodified copies for traceability

🔹 Silver Layer

Cleans data

Handles missing values

Creates derived features (e.g., revenue = quantity × price)

🔹 Gold Layer

Generates business KPIs

Computes revenue insights

Produces monthly trends

Runs loyalty segmentation

📊 Key Features
📈 Business KPIs

Total Revenue

Total Orders

Average Order Value

Monthly Revenue Trend

🏆 Product & Customer Insights

Top 5 Products by Revenue

Top 5 Customers by Revenue

💎 Loyalty Engine (RFM Analysis)

Recency (Days since last purchase)

Frequency (Number of purchases)

Monetary (Total spending)

Customer Segmentation:

Premium

Loyal

Regular

At Risk

🛠 Tech Stack

Python

Pandas

NumPy

Streamlit

Matplotlib / Plotly

Logging

Git & GitHub

📁 Project Structure
retailpulse/
│
├── data/               # Raw dataset
├── bronze/             # Raw ingested data
├── silver/             # Cleaned data
├── gold/               # KPIs & analytics outputs
├── logs/               # Log files
│
├── src/
│   ├── bronze.py
│   ├── silver.py
│   ├── gold.py
│   ├── loyalty.py
│
├── dashboard.py        # Streamlit dashboard
├── main.py             # ETL pipeline runner
├── requirements.txt
└── README.md
🚀 How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run ETL Pipeline
python main.py
4️⃣ Launch Dashboard
streamlit run dashboard.py
🎯 Business Value

RetailPulse helps businesses:

Monitor revenue performance

Identify high-value customers

Detect customer churn risk

Optimize marketing strategies

Improve customer retention

🏆 Hackathon Highlights

Structured ETL architecture (Bronze–Silver–Gold)

RFM-based customer segmentation

Interactive business dashboard

Clean, modular Python design

GitHub-ready professional repository
