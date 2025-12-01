'''import pandas as pd
s=pd.Series([1,2,3,4,5,6])
print(s)
#dataframe
data={
    "Name":["Anu","Divya","John"],
    "Marks":[85,90,95]
}
df=pd.DataFrame(data)
print(df)'''
##
import pandas as pd
#create sample data
df=pd.DataFrame(data={
    "Name":["Anu","Divya","John"],
    "Marks":[85,90,95],
    "City":["Mumbai","chennai","trichy"],
    "Age":[20,19,18]
})

'''print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.describe())'''

print(df)
print(df["Name"])
print(df[["Name","Marks"]])
#fliters
high_scores=df[df["Marks"]>70]
print(high_scores)
filtered=df[(df["Marks"]>70) & (df["Age"]>22)]
print(filtered)

df["Result"]=df["Marks"].apply(lambda x:"Pass" if x>=60 else "Fail")
print(df)
sorted_df=df.sort_values(by="Marks",ascending=False)
print(sorted_df)

df2=df.copy()
df2.loc[2,"City"]=None#create missing value
print(df2)
print(df2.isnull().sum())
df2_filled=df2.fillna("Unknown")
print(df2_filled)

city_count=df.groupby("City")["Name"].count()
print(city_count)
avg_marks=df.groupby("City")["Marks"].mean()
print(avg_marks)

'''
#write csv
df.to_csv("student.csv",index=False)#false means index value will be gone
print("CSV is created.")
#read from the same csv
import pandas as pd
df=pd.read_csv("student.csv")
print("CSV file read successfully.")
print(df)'''