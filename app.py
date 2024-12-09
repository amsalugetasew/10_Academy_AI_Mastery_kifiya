import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from dashboard import load_data, summary_stats, correlation_heatmap, plot_boxplot, plot_histogram

# App title and description
st.title("Interactive Data Insights Dashboard")
st.markdown("<p style='color:gray;'>Explore and visualize data insights dynamically.</p>", unsafe_allow_html=True)

# Sidebar for options
st.sidebar.header("My Week 0 Tenx Streamlit Dynamic Visualization Dashboard")
source = st.sidebar.selectbox("Data Source", ["local"])

# Sidebar for file upload
st.sidebar.header("Upload Data File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file to upload", type=["csv"])

# Load and process data only if a file is uploaded
if uploaded_file is None:
    st.warning("Please upload a CSV file to proceed.")
else:
    # Load and process data
    try:
        # Pass the uploaded file to the `load_data` function
        data = load_data(uploaded_file)
        
        # Display the uploaded file name
        if uploaded_file:
            st.success(f"File '{uploaded_file.name}' successfully uploaded!")
        else:
            st.warning("Using default dataset as no file is uploaded.")
        # Dropdown for views
        view_option = st.selectbox(
            "Select View",
            ["Select Option","Data Overview","Statistical Summary", "Top N Rows", "Correlation Matrix", "Correlation Map"],
        )
        # Display selected view
        if view_option == "Data Overview":
            st.header("DataFrame Info")
            # Extract details from df.info()
            df_info = pd.DataFrame({
                "Column": data.columns,
                "Non-Null Count": [data[col].notnull().sum() for col in data.columns],
                "Dtype": [data[col].dtype for col in data.columns]
            })
            st.dataframe(df_info)
        if view_option == "Select Option":
            st.header("Please select an option you want to see")
        if view_option == "Statistical Summary":
            processed_data = summary_stats(data)
            st.header("Statistical Summary")
            st.dataframe(processed_data)

        elif view_option == "Top N Rows":
            st.header("Top N Rows")
            # Slider to dynamically select the number of rows to display
            num_rows = st.slider("Select number of rows to display", min_value=1, max_value=len(data), value=5)
            st.dataframe(data.head(num_rows))

        elif view_option == "Correlation Matrix":
            try:
                corr_matrix, _ = correlation_heatmap(data, return_plot=False)
                st.header("Correlation Matrix Table")
                st.dataframe(corr_matrix)
            except Exception as e:
                st.error(f"Error displaying correlation matrix: {e}")

        elif view_option == "Correlation Map":
            try:
                _, heatmap_plot = correlation_heatmap(data)
                st.header("Correlation Heatmap")
                st.pyplot(heatmap_plot)
            except Exception as e:
                st.error(f"Error displaying correlation heatmap: {e}")

    except Exception as e:
        st.error(f"Error loading data: {e}")



    # Header for histogram visualization
    st.header("Histogram Visualization")

    try:
        # Select a column for the histogram
        selected_hist_column = st.selectbox("Select a column for the histogram", data.columns, key="histogram_dropdown")
        
        # Generate and display the histogram
        histogram_fig = plot_histogram(data, selected_hist_column)
        st.plotly_chart(histogram_fig)
        
    except Exception as e:
        st.error(f"Error displaying histogram: {e}")

    # Header for boxplot visualization
    st.header("Boxplot Visualization")

    try:
        # Select a column for the boxplot
        selected_column = st.selectbox("Select a column for the boxplot", data.columns)
        
        # Generate and display the boxplot
        boxplot_fig = plot_boxplot(data, selected_column)
        st.plotly_chart(boxplot_fig)
        
    except Exception as e:
        st.error(f"Error displaying boxplot: {e}")
