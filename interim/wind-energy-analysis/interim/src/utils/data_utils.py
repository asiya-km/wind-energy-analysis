"""
Utility functions for data processing and analysis.
"""
import pandas as pd
import numpy as np
from typing import Tuple, List
from scipy import stats

def detect_outliers(df: pd.DataFrame, columns: List[str], z_threshold: float = 3.0) -> pd.DataFrame:
    """
    Detect outliers using Z-score method.
    
    Args:
        df: Input DataFrame
        columns: List of columns to check for outliers
        z_threshold: Z-score threshold for outlier detection
        
    Returns:
        DataFrame with outlier flags
    """
    df_outliers = df.copy()
    for col in columns:
        z_scores = np.abs(stats.zscore(df[col].dropna()))
        df_outliers[f'{col}_outlier'] = z_scores > z_threshold
    return df_outliers

def clean_missing_values(df: pd.DataFrame, 
                        strategy: str = 'mean',
                        columns: List[str] = None) -> pd.DataFrame:
    """
    Clean missing values in the dataset.
    
    Args:
        df: Input DataFrame
        strategy: Strategy for imputation ('mean', 'median', 'mode', 'drop')
        columns: List of columns to clean (None for all columns)
        
    Returns:
        Cleaned DataFrame
    """
    df_clean = df.copy()
    if columns is None:
        columns = df.columns
    
    for col in columns:
        if strategy == 'drop':
            df_clean = df_clean.dropna(subset=[col])
        elif strategy == 'mean':
            df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
        elif strategy == 'median':
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        elif strategy == 'mode':
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
    
    return df_clean

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate summary statistics for the dataset.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with summary statistics
    """
    summary = pd.DataFrame({
        'count': df.count(),
        'mean': df.mean(),
        'std': df.std(),
        'min': df.min(),
        '25%': df.quantile(0.25),
        '50%': df.quantile(0.50),
        '75%': df.quantile(0.75),
        'max': df.max(),
        'missing': df.isnull().sum(),
        'missing_pct': (df.isnull().sum() / len(df)) * 100
    })
    return summary

def merge_country_data(dataframes: List[pd.DataFrame], 
                      country_names: List[str]) -> pd.DataFrame:
    """
    Merge datasets from multiple countries.
    
    Args:
        dataframes: List of DataFrames to merge
        country_names: List of country names corresponding to each DataFrame
        
    Returns:
        Merged DataFrame with country column
    """
    merged_dfs = []
    for df, country in zip(dataframes, country_names):
        df_copy = df.copy()
        df_copy['country'] = country
        merged_dfs.append(df_copy)
    
    return pd.concat(merged_dfs, ignore_index=True) 