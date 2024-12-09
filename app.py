import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dashboard import load_data, summary_stats, correlation_heatmap, plot_boxplot, filter_data

# App title and description
st.title("Interactive Data Insights Dashboard")
st.markdown("Explore and visualize data insights dynamically.")

# Sidebar for options
source = st.sidebar.selectbox("Data Source", ["local"])
slider = st.sidebar.slider("Filter Value", 0, 100, 50)

# Load and process data
try:
    data = load_data(source)
    processed_data = summary_stats(data)
    st.header("Statistical Summary")
    st.dataframe(processed_data) 
    
    # Display raw data and visualizations
    st.header("Raw Data")
    st.dataframe(data.head())

    
except Exception as e:
    st.error(f"Error loading data: {e}")
# Plot correlation heatmap and boxplot
    st.header("Correlation Matrix")

try:
    corr_matrix, heatmap_plot = correlation_heatmap(data)
    
    # Display the correlation heatmap using Matplotlib
    st.pyplot(heatmap_plot)
    
    # Display the raw correlation matrix as a table
    st.write("Correlation Matrix Table:")
    st.dataframe(corr_matrix)
    
except Exception as e:
    st.error(f"Error displaying correlation matrix: {e}")

st.header("Boxplot Visualization")

try:
    # Select a column for the boxplot
    selected_column = st.selectbox("Select a column for the boxplot", data.columns)
    
    # Generate and display the boxplot
    boxplot_fig = plot_boxplot(data, selected_column)
    st.plotly_chart(boxplot_fig)
    
except Exception as e:
    st.error(f"Error displaying boxplot: {e}")
