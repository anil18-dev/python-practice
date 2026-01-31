import pandas as pd

# 1. Load the file
df = pd.read_csv('investors.csv')

# 2. DETECTIVE WORK: Show all column names exactly as they are
print("DEBUG: The columns found in your file are:")
print(list(df.columns))
print("-" * 30)

# 3. THE MAGIC FIX: This removes quotes and spaces from the names
df.columns = df.columns.str.strip().str.replace('"', '')

# 4. Now run the report (this should work now)
try:
    report = df['PAN Number'].str[3].value_counts()
        print("--- INVESTOR STATUS REPORT ---")
            print(report)
            except KeyError:
                print("ERROR: Still can't find 'PAN Number'. Check the list above!")