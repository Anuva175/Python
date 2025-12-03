#pivot table
import pandas as pd
df=pd.read_csv("retail.csv")

#Create pivot: Rows = Region, Columns = Category, Values = Sales.
pivot=df.pivot_table(index="Region",columns="Category",values="Sales",aggfunc="sum")
print(pivot)

#Pivot showing Profit by SubCategory and Segment.
pivot_profit=df.pivot_table(index="SubCategory",columns="Segment",values="Profit",aggfunc="sum")
print(pivot_profit)

#Pivot showing count of orders by Returned status and Region.
pivot_count=df.pivot_table(index="Returned",columns="Region",values="OrderID",aggfunc="count")
print(pivot_count)

#Pivot showing average UnitPrice per Category.
