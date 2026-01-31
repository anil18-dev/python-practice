import pandas as pd

# 1. Load the data
df = pd.read_csv('investors.csv')

# 2. POWER CLEAN: Remove every single space from all column names
# ' PAN Number ' will become 'PANNumber'
df.columns = df.columns.str.replace(' ', '').str.replace('"', '')

# 3. Run the report using the name without spaces
if 'PANNumber' in df.columns:
    # We also clean the actual data in the rows
    report = df['PANNumber'].str.strip().str[3].value_counts()
    print('--- SUCCESS: INVESTOR STATUS REPORT ---')
    print(report)
else:
    print('ERROR: Still cannot find the column. Columns found:')
    print(df.columns.tolist())
