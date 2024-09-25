import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file = r"C:\Users\Yousuf Traders\Desktop\Ayesha python\DEN projects\SaleData.xlsx"
df = pd.read_excel(file)

# These display the first and last few rows, describe the data, and print info and null counts
print(df.head() )
print("\n")
print(df.tail())
print("\n")
print(df.describe())
print("\n")
print(df.info())
print("\n")
print(df.isnull().sum())
print("\n")

# Extract the year from the OrderDate column
df['Order Year'] = pd.to_datetime(df['OrderDate']).dt.year

# Count the number of orders per year and sort the index
year_counts = df['Order Year'].value_counts().sort_index()

# Plot the data
plt.figure(figsize=(10, 6))
data = year_counts.plot(kind='bar', color='darkblue')
data.set_facecolor('beige')
plt.title('Number of Items Per Year')
plt.xlabel('Years')
plt.ylabel('Items')
plt.tight_layout()  
plt.show()  

# count the number of units per item and plot them
item_counts = df['Item'].value_counts().sort_index()
plt.figure(figsize=(12,6))
data2 = item_counts.plot(kind='line', marker='o' ,linestyle='-', color='red')
data2.set_facecolor('beige')
plt.title('Number of units per item')
plt.xlabel('Items')
plt.ylabel('Units')
plt.tight_layout()
plt.show()