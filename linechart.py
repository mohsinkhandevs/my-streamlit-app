import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page Configuration (changes browser tab header from Streamlit to EDA Dashboard)
st.set_page_config(page_title="EDA Dashboard", page_icon="📊")

# Page Title
st.title("EDA Dashboard")
st.caption("Exploratory Data Analysis Interface")

# Sidebar - Dataset Controls
st.sidebar.title("EDA Dashboard")
st.sidebar.header("Dataset Controls")
uploaded_file = st.sidebar.file_uploader("Upload CSV File for Analysis", type=["csv"])

# Load Dataset: from uploaded file, or default file if present
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
elif os.path.exists("data/Titanic-Dataset.csv"):
    df = pd.read_csv("data/Titanic-Dataset.csv")
else:
    df = None

# If a dataset is available, display dashboard
if df is not None:
    # Sidebar - Attribute Selection
    st.sidebar.header("Attribute Selection")
    columns = list(df.columns)
    default_idx = columns.index("Age") if "Age" in columns else 0
    selected_col = st.sidebar.selectbox("Select Attribute for Visualization", columns, index=default_idx)

    # Automated Attribute Typing
    if pd.api.types.is_numeric_dtype(df[selected_col]):
        col_type = "Numerical"
    else:
        col_type = "Categorical"

    st.sidebar.write(f"**Detected Type:** {col_type}")

    # Main Content - Dataset Preview & Metadata
    st.header("Dataset Preview & Metadata")

    st.subheader("First 5 Rows:")
    st.dataframe(df.head(5))

    st.write(f"**Shape:** `{df.shape}`")

    st.subheader("Column Data Types:")
    dtypes_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })
    st.dataframe(dtypes_df)

    st.subheader("Missing Values per Column:")
    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": df.isnull().sum().values,
        "Missing %": ((df.isnull().sum() / len(df)) * 100).round(4).values
    })
    st.dataframe(missing_df)

    st.subheader("Statistical Summary (Numerical Attributes):")
    numeric_summary = df.describe().T[["mean", "50%", "min", "max"]].rename(columns={"50%": "median"})
    st.dataframe(numeric_summary)

    # Main Content - Visualization Module
    st.header("Visualization")

    if col_type == "Numerical":
        st.subheader(f"Histogram of {selected_col}")
        fig, ax = plt.subplots()
        ax.hist(df[selected_col].dropna(), bins=20, edgecolor="black", color="skyblue")
        ax.set_title(f"Histogram of {selected_col}")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    else:
        st.subheader(f"Bar Chart of {selected_col}")
        fig, ax = plt.subplots()
        df[selected_col].value_counts().plot(kind="bar", ax=ax, edgecolor="black", color="salmon")
        ax.set_title(f"Bar Chart of {selected_col}")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
else:
    st.info("Please upload a CSV file from the sidebar to begin analysis.")
