import pandas as pd
from openpyxl import load_workbook

# Paths to the files
existing_file_path = 'path_to_existing_excel_file.xlsx'
new_file_path = 'path_to_new_excel_file.xlsx'

# Load the existing Excel file
book = load_workbook(existing_file_path)

# Load the first sheet of the new Excel file using pandas
df = pd.read_excel(new_file_path, sheet_name=0)

# Name of the new sheet where data will be added
new_sheet_name = 'ImportedSheet'

# Add the dataframe to the existing workbook as a new sheet
with pd.ExcelWriter(existing_file_path, engine='openpyxl', mode='a') as writer:
    writer.book = book
    df.to_excel(writer, sheet_name=new_sheet_name, index=False)

# Save the modified workbook
book.save(existing_file_path)

print(f'Successfully added {new_sheet_name} and saved changes to {existing_file_path}')
