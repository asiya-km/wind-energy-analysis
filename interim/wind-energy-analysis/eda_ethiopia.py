import pandas as pd
from data_utils import get_summary_stats, clean_missing_values

# Load sample data
df = pd.read_csv("data/raw/ethiopia_wind.csv")

# Clean and summarize
df_clean = clean_missing_values(df)
summary = get_summary_stats(df_clean)

print(summary)
