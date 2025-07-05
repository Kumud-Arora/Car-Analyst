import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin-1")
    df = df.rename(columns={"kilometer": "mileage"})
    df["registration_date"] = pd.to_datetime(
        dict(
            year=df.yearOfRegistration,
            month=df.monthOfRegistration,
            day=1
        ),
        errors="coerce"
    )
    df["region"] = df.postalCode.astype(str)
    return df

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df["mileage"].fillna(df["mileage"].median(), inplace=True)
    df.dropna(subset=["price", "model"], inplace=True)
    return df

def normalize(df: pd.DataFrame) -> pd.DataFrame:
    scaler = MinMaxScaler()
    df[["price_norm", "mileage_norm"]] = scaler.fit_transform(
        df[["price", "mileage"]]
    )
    return df
