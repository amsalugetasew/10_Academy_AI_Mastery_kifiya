import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dashboard import load_data, summary_stats, correlation_heatmap, plot_boxplot, filter_data

# App title and description
st.title("Interactive Data Insights Dashboard")
st.markdown("Explore and visualize data insights dynamically.")

# Sidebar for options
source = st.sidebar.selectbox("Data Source", ["local", "api"])
slider = st.sidebar.slider("Filter Value", 0, 100, 50)

# Load and process data
try:
    data = load_data(source)
    processed_data = summary_stats(data)
    
    # Display raw data and visualizations
    st.header("Raw Data")
    st.dataframe(data)
    
    # Plot correlation heatmap and boxplot
    correlation_heatmap(data)
    plot_boxplot(data, data.columns[0])  # Adjust the column as needed

    # Filter the data based on slider value
    st.header("Filtered Data")
    filtered_data = filter_data(data, data.columns)
    st.dataframe(filtered_data)
    
    # Display histogram for filtered data
    st.header("Visualizations")
    fig, ax = plt.subplots()
    filtered_data["processed_column"] = pd.to_numeric(filtered_data["processed_column"], errors="coerce")
    filtered_data["processed_column"].plot(kind="hist", ax=ax)
    st.pyplot(fig)
    
except Exception as e:
    st.error(f"Error loading data: {e}")
