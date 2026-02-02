"""
Project: Automated Investor Data Analysis (5,500+ Records)
Author: Anil Dangi
Description: Advanced cleaning pipeline for broken/quoted CSV files.
"""
import pandas as pd
import os
import io

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, 'investors.csv')
output_path = os.path.join(base_path, 'client_report.txt')

try:
    # 1. THE BRUTE FORCE CLEANUP
    # We read the file as raw text to remove the "Quote Trap"
    with open(csv_path, 'r') as f:
        lines = f.readlines()
    
    # Remove " quotes from every line and then join them back together
    clean_data = "".join([line.replace('"', '') for line in lines])
    
    # 2. LOAD THE CLEANED DATA
    # Use io.StringIO to make the clean text look like a file to Pandas
    df = pd.read_csv(io.StringIO(clean_data))
    
    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()
    
    # 3. VERIFY AND PROCESS
    target_col = 'PAN Number'
    if target_col not in df.columns:
        print(f"Error: Could not find '{target_col}'. Found columns: {list(df.columns)}")
        exit()

    # Extract 4th character (Index 3) and clean spaces
    df['Status_Code'] = df[target_col].str.strip().str[3].str.upper()

    # 4. MAP DESCRIPTIONS
    status_map = {'P': 'Individual', 'C': 'Company', 'H': 'HUF', 'F': 'Firm', 'A': 'AOP', 'T': 'Trust'}
    df['Status_Description'] = df['Status_Code'].map(status_map).fillna('Other')

    # 5. OUTPUT
    report = df['Status_Description'].value_counts()
    print("\n--- INVESTOR STATUS REPORT ---")
    print(report)

    with open(output_path, 'w') as f:
        f.write("--- INVESTOR STATUS REPORT ---\n")
        f.write(report.to_string())
    
    print(f"\nSUCCESS: Report saved to {output_path}")

except Exception as e:
    print(f"\nCRITICAL ERROR: {e}")

