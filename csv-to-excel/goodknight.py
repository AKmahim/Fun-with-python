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









# ============================================

import pandas as pd

# Read the Excel file
excel_file = 'gdn-product-code.xlsx'
df = pd.read_excel(excel_file)

# Rename columns
df.columns = ['sl', 'product-code']

# Create SQL dump file
sql_dump_file = 'gdn-product-code.sql'

# Write SQL statements to the file
with open(sql_dump_file, 'w') as f:
    f.write("-- phpMyAdmin SQL Dump\n")
    f.write("-- version 5.1.1deb5ubuntu1\n")
    f.write("-- https://www.phpmyadmin.net/\n")
    f.write("--\n")
    f.write("-- Host: localhost:3306\n")
    f.write("-- Generation Time: Apr 23, 2024 at 04:07 AM\n")
    f.write("-- Server version: 8.0.36-0ubuntu0.22.04.1\n")
    f.write("-- PHP Version: 8.1.2-1ubuntu2.14\n")
    f.write("\n")
    f.write("SET SQL_MODE = \"NO_AUTO_VALUE_ON_ZERO\";\n")
    f.write("START TRANSACTION;\n")
    f.write("SET time_zone = \"+00:00\";\n")
    f.write("\n")
    f.write("/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;\n")
    f.write("/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;\n")
    f.write("/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;\n")
    f.write("/*!40101 SET NAMES utf8mb4 */;\n")
    f.write("\n")
    f.write("--\n")
    f.write("-- Database: `goodnight`\n")
    f.write("--\n")
    f.write("\n")
    f.write("-- --------------------------------------------------------\n")
    f.write("--\n")
    f.write("-- Table structure for table `product_codes`\n")
    f.write("--\n")
    f.write("\n")
    f.write("CREATE TABLE `product_codes` (\n")
    f.write("  `id` INT AUTO_INCREMENT PRIMARY KEY,\n")
    f.write("  `product_code` INT\n")
    f.write(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;\n")
    f.write("\n")
    f.write("--\n")
    f.write("-- Dumping data for table `your_table_name`\n")
    f.write("--\n")
    for index, row in df.iterrows():
        f.write(f"INSERT INTO `your_table_name` (`product_code`) VALUES ({row['product-code']});\n")
    f.write("\n")
    f.write("/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;\n")
    f.write("/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;\n")
    f.write("/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;\n")
    f.write("\n")
    f.write("COMMIT;\n")

print(f'SQL dump file "{sql_dump_file}" has been created successfully.')
