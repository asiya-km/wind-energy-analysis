"""
Utility functions for data visualization.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Optional

def plot_time_series(df: pd.DataFrame, 
                    date_col: str,
                    value_col: str,
                    title: str = "Time Series Plot") -> go.Figure:
    """
    Create an interactive time series plot.
    
    Args:
        df: Input DataFrame
        date_col: Name of the date column
        value_col: Name of the value column
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    fig = px.line(df, x=date_col, y=value_col, title=title)
    return fig

def plot_wind_distribution(df: pd.DataFrame,
                          wind_col: str,
                          title: str = "Wind Distribution") -> go.Figure:
    """
    Create a wind distribution plot.
    
    Args:
        df: Input DataFrame
        wind_col: Name of the wind speed column
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    fig = px.histogram(df, x=wind_col, title=title)
    return fig

def plot_correlation_matrix(df: pd.DataFrame,
                           columns: Optional[List[str]] = None) -> go.Figure:
    """
    Create a correlation matrix heatmap.
    
    Args:
        df: Input DataFrame
        columns: List of columns to include (None for all numeric columns)
        
    Returns:
        Plotly figure object
    """
    if columns is None:
        columns = df.select_dtypes(include=['float64', 'int64']).columns
    
    corr_matrix = df[columns].corr()
    fig = px.imshow(corr_matrix,
                   labels=dict(color="Correlation"),
                   x=columns,
                   y=columns,
                   title="Correlation Matrix")
    return fig

def plot_boxplot_by_country(df: pd.DataFrame,
                           value_col: str,
                           country_col: str = 'country',
                           title: str = "Boxplot by Country") -> go.Figure:
    """
    Create a boxplot comparing values across countries.
    
    Args:
        df: Input DataFrame
        value_col: Name of the value column
        country_col: Name of the country column
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    fig = px.box(df, x=country_col, y=value_col, title=title)
    return fig

def plot_bubble_chart(df: pd.DataFrame,
                     x_col: str,
                     y_col: str,
                     size_col: str,
                     color_col: Optional[str] = None,
                     title: str = "Bubble Chart") -> go.Figure:
    """
    Create an interactive bubble chart.
    
    Args:
        df: Input DataFrame
        x_col: Name of the x-axis column
        y_col: Name of the y-axis column
        size_col: Name of the column to use for bubble size
        color_col: Name of the column to use for bubble color
        title: Plot title
        
    Returns:
        Plotly figure object
    """
    fig = px.scatter(df,
                    x=x_col,
                    y=y_col,
                    size=size_col,
                    color=color_col,
                    title=title)
    return fig 