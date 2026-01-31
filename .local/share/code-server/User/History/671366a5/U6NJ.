import pandas as pd

# 1. Load the data file
df = pd.read_csv('investors.csv')

# 2. Count the 4th character of every PAN number
# This is the "Magic" line
report = df['PAN Number'].str[3].value_counts()

# 3. Show the final result
print("--- INVESTOR STATUS REPORT ---")
print(report)