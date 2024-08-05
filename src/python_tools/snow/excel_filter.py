import pandas as pd

# Example DataFrame
data = {
    "Name": ["John", "Anna", "Mike", "Sara", "Tom"],
    "Age": [25, 30, 35, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago", "New York", "Chicago"],
}
df = pd.DataFrame(data)

# Write the DataFrame to Excel without applying any filter in pandas
with pd.ExcelWriter("filtered_example_xlsxwriter.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)

    # Access the XlsxWriter workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets["Sheet1"]

    # Apply an AutoFilter to the range of data
    worksheet.autofilter(0, 0, len(df), len(df.columns) - 1)

    # Apply a filter condition for the "City" column (3rd column, so index 2)
    worksheet.filter_column(2, 'x == "Chicago" or x == "New York"')
