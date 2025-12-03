import pandas as pd
df=pd.read_csv("retail.csv")
print(df.head(10))
print(df)
print(df.info())
print(df.columns[df.isnull().any()])
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
print(df.info())
#Ex-2
df["ShippingDays"]=(df["ShipDate"]-df["OrderDate"]).dt.days
print(df["ShippingDays"])
#profitMargin
df["ProfitMargin"]=df["Profit"]/df["Sales"]
print(df["ProfitMargin"])
#Standardize customername
df["CustomerName"]=df["CustomerName"].str.title()
print(df["CustomerName"])
#remove rows where sales<=0
df=df[df["Sales"]>0]
print(df.head())
#convert discount to percentage
df["Discount"]=(df["Discount"]*100).round(2).astype(str)+'%'
print(df["Discount"])

#Filter all orders from the west region
new_order=df[df["Region"]=="West"]
print(new_order)
#Filter Technology category with Sales > 400.
technology=df[(df["Category"]=="Technology") &(df["Sales"]>400)]
print(technology)
#Find all products returned by customers
returned=df[df["Returned"]=="Yes"]["ProductName"]
print(returned)
#Show Furniture orders shipped after 2024-01-20.
shipped=df[(df["Category"]=="Furniture")&(df["ShipDate"]>"2024-01-20")]
print(shipped)
#Filter orders where Profit < 20.
gain=df[(df["Profit"]<20)]
print(gain)

#Sort by Sales descending.
sort_sales=df.sort_values(by="Sales",ascending=False)
print(sort_sales)
#Sort by ProfitMargin.
sort_margin=df.sort_values("ProfitMargin",ascending=False)
print(sort_margin)
#Sort by Region then City.
sort_region=df.sort_values("Region",ascending=False)
print(sort_region)
sort_city=df.sort_values("City",ascending=False)
print(sort_city)
#Sort by ShippingDays largest to smallest.
sort_shipdate=df.sort_values("ShipDate",ascending=False)
print(sort_shipdate)
#Sort by CustomerName alphabetical.
sort_custname=df.sort_values("CustomerName",ascending=False)
print(sort_custname)

#Groupby Total Sales per Region.
total_sales=df.groupby("Region")["Sales"].sum()#sum->total
print(total_sales)
#Average Profit per Category
avg_profit=df.groupby("Category")["Profit"].mean()
print(avg_profit)
#Count of orders per Customer.
order_count = df.groupby("CustomerID").size()
print(order_count)
#Sum of Sales per Segment.
sum_sales=df.groupby("Segment")["Sales"].sum()
print(sum_sales)
#Total Quantity sold per SubCategory.
tot_quantity=df.groupby("SubCategory")["Quantity"].sum()
print(tot_quantity)
#Mean ShippingDays grouped by Category.
mean_ship=df.groupby("Category")["ShipDate"].mean()
print(mean_ship)

