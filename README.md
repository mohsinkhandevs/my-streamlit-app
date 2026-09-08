# EDA Dashboard

A minimal, interactive Exploratory Data Analysis (EDA) dashboard built with Streamlit.

## Features

- **Dataset Ingestion**: Upload any CSV dataset or use the default Titanic dataset.
- **Dataset Overview**:
  - Preview first 5 rows
  - Dataset shape (rows & columns)
  - Column data types
  - Missing values count & percentage
  - Statistical summary for numerical attributes (mean, median, min, max)
- **Attribute Visualization**:
  - **Numerical Attributes**: Value distribution histogram with frequency count.
  - **Categorical Attributes**: Frequency count bar chart.

## Project Structure

```
Lab-04/
├── data/
│   └── Titanic-Dataset.csv     # Sample dataset
├── linechart.py                # Main Streamlit application
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Setup & Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   streamlit run linechart.py
   ```
