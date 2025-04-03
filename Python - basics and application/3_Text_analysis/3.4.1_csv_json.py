import pandas as pd
import datetime
from pathlib import Path

BASE_DIR = Path("__file__").resolve().parent.parent
FILENAME = Path.joinpath(BASE_DIR, "./Crimes.csv")


data = pd.read_csv(FILENAME)
# print(data.head())
data["Date"] = pd.to_datetime(data["Date"])
# print(data.columns)
# print(data.head())
data_15 = data[(data['Date'] >= "2015-01-01") & (data['Date']<= "2015-12-31")]
# print(data_15.head())
# print(data_15.groupby(["Primary Type"]).count())
pt = data_15.pivot_table(index=["Primary Type"], aggfunc="count")
print(pt[pt["ID"] == pt["ID"].max()])