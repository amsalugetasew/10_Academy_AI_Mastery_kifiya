import pandas as pd
import requests

# Load data
def load_data(source: str):
    if source == "local":
        df = pd.read_csv("data/benin-malanville.csv")
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])  # Ensure Timestamp is in datetime format
        return df
    elif source == "api":
        url = "https://api.example.com/data"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])  # Ensure Timestamp is in datetime format
        return df
    else:
        raise ValueError("Invalid data source")

# Generate summary statistics
def summary_stats(df):
    return df.describe()

# Filter data based on processed column value
def filter_data(df, threshold):
    df["processed_column"] = pd.to_numeric(df["processed_column"], errors="coerce")  # Convert to numeric
    return df[df["processed_column"] < threshold]

# Plot correlation heatmap
def correlation_heatmap(df):
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    return plt

# Plot boxplot for numerical column
def plot_boxplot(df, column):
    import plotly.express as px
    df[column] = pd.to_numeric(df[column], errors="coerce")  # Convert to numeric, non-numeric values will be set to NaN
    fig = px.box(df, y=column, title=f"Boxplot of {column}")
    return fig
