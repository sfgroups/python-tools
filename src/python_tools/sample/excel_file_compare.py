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
#======

import pandas as pd

def compare_and_add_column(file1, file2, column_to_match, column_to_check):
  """
  Reads two Excel files, compares values in the first column of the first file with the first row of the second file,
  checks if the corresponding row in the second file contains 'Cyber' in column D,
  and adds a new column to the first file indicating whether the values match.

  Args:
    file1: Path to the first Excel file.
    file2: Path to the second Excel file.
    column_to_match: Name of the column in the first file to match with the first row of the second file.
    column_to_check: Name of the column in the second file to check for 'Cyber'.

  Returns:
    The modified first DataFrame with the new column.
  """

  df1 = pd.read_excel(file1)
  df2 = pd.read_excel(file2)

  # Convert the first row of df2 to a dictionary for efficient lookup
  lookup_dict = df2.iloc[0].to_dict()

  # Create a new column in df1 to store the match results
  df1['Match'] = 'No'

  # Iterate over rows in df1 and check for matches
  for index, row in df1.iterrows():
    value_to_match = row[column_to_match]
    if value_to_match in lookup_dict:
      matching_row = df2[df2.columns[0] == value_to_match]
      if not matching_row.empty and 'Cyber' in matching_row[column_to_check].values:
        df1.at[index, 'Match'] = 'Yes'

  return df1

# Example usage
file1_path = 'file1.xlsx'
file2_path = 'file2.xlsx'
column_to_match = 'ColumnA'  # Replace with the actual column name
column_to_check = 'D'  # Replace with the actual column name

result_df = compare_and_add_column(file1_path, file2_path, column_to_match, column_to_check)
print(result_df)
