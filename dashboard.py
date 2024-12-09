import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data dynamically based on user upload 
def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)  # Load the uploaded CSV file
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])  # Ensure Timestamp is in datetime format
        return df
    else:
        raise ValueError("No file uploaded. Please upload a CSV file.")
# Generate summary statistics
def summary_stats(df):
    return df.describe()

# Filter data based on processed column value
def filter_data(df, threshold):
    df["processed_column"] = pd.to_numeric(df["GHI"] * 0.1 , errors="coerce")  # Convert to numeric
    return df[df["processed_column"] < threshold]

def correlation_heatmap(df):
    corr_matrix = df.corr()  # Compute the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    return corr_matrix, plt
# Plot boxplot for numerical column
def plot_boxplot(df, column):
    import plotly.express as px
    df[column] = pd.to_numeric(df[column], errors="coerce")  # Convert to numeric, non-numeric values will be set to NaN
    fig = px.box(df, y=column, title=f"Boxplot of {column}")
    return fig
def plot_boxplot(df, column):
    fig = px.box(df, y=column, title=f"Boxplot of {column}")
    return fig
# Function to plot histogram
def plot_histogram(df, column):
    fig = px.histogram(df, x=column, title=f"Histogram of {column}", nbins=30)
    return fig