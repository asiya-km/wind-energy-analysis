"""
Streamlit app for wind energy data analysis.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import sys

# Add src directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.visualization.plot_utils import (
    plot_time_series,
    plot_wind_distribution,
    plot_correlation_matrix,
    plot_boxplot_by_country,
    plot_bubble_chart
)

def load_data():
    """Load and merge data from all countries."""
    data_dir = Path(__file__).parent.parent / 'data' / 'processed'
    dfs = []
    countries = []
    
    for file in data_dir.glob('*_cleaned.csv'):
        country = file.stem.split('_')[0]
        df = pd.read_csv(file)
        dfs.append(df)
        countries.append(country)
    
    return pd.concat(dfs, keys=countries, names=['country']).reset_index()

def main():
    st.title("Wind Energy Analysis Dashboard")
    
    # Load data
    try:
        df = load_data()
        st.success("Data loaded successfully!")
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return
    
    # Sidebar controls
    st.sidebar.header("Controls")
    
    # Country selection
    countries = df['country'].unique()
    selected_countries = st.sidebar.multiselect(
        "Select Countries",
        countries,
        default=countries
    )
    
    # Filter data based on selection
    df_filtered = df[df['country'].isin(selected_countries)]
    
    # Visualization selection
    viz_type = st.sidebar.selectbox(
        "Select Visualization",
        ["Time Series", "Wind Distribution", "Correlation Matrix", 
         "Boxplot by Country", "Bubble Chart"]
    )
    
    # Display selected visualization
    if viz_type == "Time Series":
        st.subheader("Time Series Analysis")
        date_col = st.selectbox("Select Date Column", df.columns)
        value_col = st.selectbox("Select Value Column", df.columns)
        fig = plot_time_series(df_filtered, date_col, value_col)
        st.plotly_chart(fig)
        
    elif viz_type == "Wind Distribution":
        st.subheader("Wind Distribution")
        wind_col = st.selectbox("Select Wind Column", df.columns)
        fig = plot_wind_distribution(df_filtered, wind_col)
        st.plotly_chart(fig)
        
    elif viz_type == "Correlation Matrix":
        st.subheader("Correlation Matrix")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        selected_cols = st.multiselect("Select Columns", numeric_cols, default=numeric_cols[:5])
        if selected_cols:
            fig = plot_correlation_matrix(df_filtered, selected_cols)
            st.plotly_chart(fig)
            
    elif viz_type == "Boxplot by Country":
        st.subheader("Boxplot by Country")
        value_col = st.selectbox("Select Value Column", df.columns)
        fig = plot_boxplot_by_country(df_filtered, value_col)
        st.plotly_chart(fig)
        
    elif viz_type == "Bubble Chart":
        st.subheader("Bubble Chart")
        x_col = st.selectbox("Select X-axis Column", df.columns)
        y_col = st.selectbox("Select Y-axis Column", df.columns)
        size_col = st.selectbox("Select Size Column", df.columns)
        color_col = st.selectbox("Select Color Column", df.columns)
        fig = plot_bubble_chart(df_filtered, x_col, y_col, size_col, color_col)
        st.plotly_chart(fig)
    
    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(df_filtered.describe())

if __name__ == "__main__":
    main() 