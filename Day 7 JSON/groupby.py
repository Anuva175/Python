import pandas as pd
df=pd.read_csv("students.csv")

high_elec=df[(df["Category"]=="Electronics")&(df["TotalPrice"]>10000)]
print(high_elec)

sorted_df=df.sort_values("TotalPrice",ascending=False)
print(sorted_df)

category_sales=df.groupby("Category")["TotalPrice"].sum()#sum->total
print(category_sales)

store_avg=df.groupby("Store")["TotalPrice"].mean()#mean-average
print(store_avg)

city_orders=df.groupby("City")["OrderID"].count()
print(city_orders)
