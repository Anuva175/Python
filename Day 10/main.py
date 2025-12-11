import pandas as pd
from datetime import date,timedelta,time,datetime
df["days_left"] = (pd.to_datetime(df["expiry_date"])