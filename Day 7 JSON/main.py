import pandas as pd

df=pd.DataFrame({
    "Name":["Anu","Divya","John"],
    "Marks":[85,92,78],
    "City":["Mumbai","Delhi","Chennai"]
})
df.to_json("students.json",orient="records",indent=4)
print("JSON file created.")

df=pd.read_json("students.json")
print("JSON file read successfully.")
print(df)