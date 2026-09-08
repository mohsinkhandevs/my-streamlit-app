# EDA Dashboard

An interactive Exploratory Data Analysis (EDA) dashboard built with Streamlit.

## Features

- **Dataset Ingestion**: Upload any CSV dataset for analysis.
- **Dataset Overview**:
  - Preview first 5 rows
  - Dataset shape (rows & columns)
  - Column data types
  - Missing values count & percentage
  - Statistical summary for numerical attributes (mean, median, min, max)
- **Attribute Visualization**:
  - **Numerical Attributes**: Value distribution histogram with frequency count.
  - **Categorical Attributes**: Frequency count bar chart.

## Setup & Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   streamlit run linechart.py
   ```
