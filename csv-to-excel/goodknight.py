# =============================== covert excel to sql file ===============================
# import pandas as pd

# # Read the Excel file
# excel_file = 'gdn-product-code.xlsx'
# df = pd.read_excel(excel_file)

# # Rename columns
# df.columns = ['sl', 'product-code']

# # Create SQL file
# sql_file = 'product_codes.sql'

# # Write SQL statements to the file
# with open(sql_file, 'w') as f:
#     f.write('CREATE TABLE IF NOT EXISTS product_codes (id INT AUTO_INCREMENT PRIMARY KEY, product_code VARCHAR(255));\n')
#     for index, row in df.iterrows():
#         f.write(f"INSERT INTO product_codes (product_code) VALUES ('{row['product-code']}');\n")

# print(f'SQL file "{sql_file}" has been created successfully.')



