# Technip Energies Sentiment Dashboard 📊

An end-to-end data analytics solution that transforms unstructured employee feedback into actionable business intelligence. This project uses **Python (NLTK)** for Natural Language Processing and **Power BI** for interactive visualization.

![Dashboard Preview](path-to-your-screenshot.png) 
*(Tip: Upload a screenshot of your "Executive Summary" page here)*

## 🚀 Project Overview

The goal of this project was to analyze unstructured feedback from global Technip Energies project hubs (Paris, Houston, Abu Dhabi, etc.) to identify **critical operational risks** and **sentiment trends**.

Instead of simple "Positive/Negative" analysis, this system implements a custom **Rule-Based AI Engine** that:
1.  **Categorizes** feedback into business units (HSE, IT, Procurement, etc.).
2.  **Calculates Severity (1-5)** based on keywords (e.g., "Fire", "Crash") and sentiment intensity.
3.  **Geolocates** data for map-based risk visualization.

## 🛠️ Tech Stack

* **Python:** Data Cleaning, Feature Engineering.
* **Libraries:** `pandas` (Data Manipulation), `nltk.VADER` (Sentiment Analysis).
* **Power BI:** Data Visualization, DAX Measures, Interactive Dashboards.
* **Data Source:** Simulated unstructured CSV data (100 rows).

## 🧠 Business Logic (The "Brain")

The Python script (`process_data.py`) enriches the raw text with the following logic:

| Feature | Logic |
| :--- | :--- |
| **Sentiment Analysis** | Uses VADER (Valence Aware Dictionary) to score text from -1 to +1. |
| **AI Categorization** | Scans for domain-specific keywords (e.g., *"PPE"* -> **HSE**, *"Server"* -> **IT**). |
| **Severity Score** | **1 (Low)** to **5 (Critical)**. A score of 5 is triggered by high-risk keywords (e.g., "Danger", "Malfunction") combined with negative sentiment. |
| **Geospatial Data** | Maps city names to specific Latitude/Longitude coordinates for visualization. |

## 📊 Dashboard Structure

The Power BI report consists of three strategic views:

### 1. Executive Summary (The Health Check)
* **Goal:** High-level view of Global Sentiment and Critical Alerts.
* **Key Visuals:** KPI Cards (Total Volume, Sentiment Score), Trend Line, Departmental Performance.

### 2. Geographic Intelligence (The "Where")
* **Goal:** Compare performance across global hubs.
* **Key Visuals:** Geospatial Map (Bubble Size = Severity), Risk Treemap.

### 3. Action Dashboard (Operational Details)
* **Goal:** Root cause analysis for project managers.
* **Key Visuals:** Word Cloud (Key Themes), Risk Heatmap, Severity Gauge, Source Funnel.

## 📥 How to Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/technip-energies-sentiment-dashboard.git](https://github.com/your-username/technip-energies-sentiment-dashboard.git)
    ```

2.  **Install Dependencies**
    ```bash
    pip install pandas nltk
    ```

3.  **Run the ETL Script**
    This script reads `ten_feedback_data.csv` and generates the enriched dataset.
    ```bash
    python process_data.py
    ```

4.  **Open in Power BI**
    * Open `Technip_Dashboard.pbix` (or import `refined_ten_dashboard_data.csv`).
    * Ensure Map visuals are configured with "Country", "Latitude", and "Longitude" data categories.

## 📂 Repository Structure

* `process_data.py`: Main Python script for NLP and data processing.
* `ten_feedback_data.csv`: Raw input data (Unstructured text).
* `refined_ten_dashboard_data.csv`: Output data ready for Power BI.
* `README.md`: Project documentation.

---
*Disclaimer: This project uses simulated data for demonstration purposes.*
