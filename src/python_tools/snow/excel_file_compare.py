import pandas as pd

# Load the two Excel files into DataFrames
file1 = 'path_to_first_excel_file.xlsx'
file2 = 'path_to_second_excel_file.xlsx'

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

# Ensure the columns to match are named the same (e.g., "Column1")
# If they have different names, rename them before comparison
# For example: df2.rename(columns={'OtherName': 'Column1'}, inplace=True)

# Match based on the first column and add a new column for the result
df1['Match'] = df1.iloc[:, 0].isin(df2.iloc[:, 0]).map({True: 'Yes', False: 'No'})

# Save the resulting DataFrame to a new Excel file
output_file = 'matched_output.xlsx'
df1.to_excel(output_file, index=False)

print(f"Comparison complete. Results saved to {output_file}")
