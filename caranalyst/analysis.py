import pandas as pd

def compute_price_by_model(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("model")["price"].agg(mean="mean", count="count").sort_values("count", ascending=False)
    )

def compute_sales_by_region(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region")["price"].count().sort_values(ascending=False)
