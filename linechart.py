import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="EDA Dashboard", page_icon="📊")

st.title("EDA Dashboard")
st.caption("Exploratory Data Analysis Interface")

st.sidebar.title("EDA Dashboard")
st.sidebar.header("Dataset Controls")
file = st.sidebar.file_uploader("Upload CSV File for Analysis", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
elif os.path.exists("data/Titanic-Dataset.csv"):
    df = pd.read_csv("data/Titanic-Dataset.csv")
else:
    df = None

if df is not None:
    st.sidebar.header("Attribute Selection")
    cols = list(df.columns)
    default_idx = cols.index("Age") if "Age" in cols else 0
    selected_col = st.sidebar.selectbox("Select Attribute for Visualization", cols, index=default_idx)

    if pd.api.types.is_numeric_dtype(df[selected_col]):
        col_type = "Numerical"
    else:
        col_type = "Categorical"

    st.sidebar.write(f"**Detected Type:** {col_type}")

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
    num_summary = df.describe().T[["mean", "50%", "min", "max"]].rename(columns={"50%": "median"})
    st.dataframe(num_summary)

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
