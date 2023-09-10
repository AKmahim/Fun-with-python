import csv
import os
import pandas as pd


# ============ convert xlsx file into csv code=======
# xlsx_folder = 'raw_data'  # Replace with the path to your folder containing XLSX files
# csv_folder = 'csv_file'    # Replace with the path where you want to save CSV files

# # Create the CSV folder if it doesn't exist
# if not os.path.exists(csv_folder):
#     os.makedirs(csv_folder)

# # Loop through each XLSX file in the folder
# for filename in os.listdir(xlsx_folder):
#     if filename.endswith('.xlsx'):
#         xlsx_path = os.path.join(xlsx_folder, filename)
#         csv_filename = os.path.splitext(filename)[0] + '.csv'
#         csv_path = os.path.join(csv_folder, csv_filename)

#         # Read XLSX file using pandas
#         df = pd.read_excel(xlsx_path)

#         # Save DataFrame as CSV file
#         df.to_csv(csv_path, index=False)

# print("Conversion completed.")

# ===================== excel to csv convert end ======================




# ================== reverse the csv file bottom to up ====
# def read_csv_reverse(file_path):
#     with open(file_path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         data = list(reader)
#         header = data[0]  # Extract the header row
#         reversed_data = list(reversed(data[1:]))  # Exclude the header row while reversing
#         return header, reversed_data

# def write_csv_reversed(file_path, header, data):
#     with open(file_path, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(header)  # Write the header row
#         writer.writerows(data)   # Write the reversed data rows

# if __name__ == "__main__":
#     input_folder = "csv_file"
#     output_folder = "reverse_file"

#     try:
#         # Create the output folder if it doesn't exist
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         for filename in os.listdir(input_folder):
#             if filename.endswith('.csv'):
#                 input_csv_file_path = os.path.join(input_folder, filename)
#                 output_csv_file_path = os.path.join(output_folder, filename)

#                 try:
#                     header, reversed_csv_data = read_csv_reverse(input_csv_file_path)
#                     write_csv_reversed(output_csv_file_path, header, reversed_csv_data)
#                     print(f"New CSV file with reversed data has been created for {filename}.")
#                 except Exception as e:
#                     print(f"An error occurred while processing {filename}: {e}")
#     except FileNotFoundError:
#         print("Folder not found. Please check the folder path.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# ================ end of reverse process code ============


# ================= sort out comment and reply =======================

# def process_csv(input_csv_file_path, output_csv_file_path):
#     # Read the CSV data into a pandas DataFrame
#     data = pd.read_csv(input_csv_file_path)

#     # Create a dictionary to store comments and their replies
#     comment_dict = {}

#     # Iterate through the DataFrame (excluding the last row)
#     for i in range(len(data) - 1):
#         # Check if the "Comment Count" is greater than 0
#         if data.loc[i, 'Comment Count'] > 0:
#             # Check if the comment already exists in the dictionary
#             if data.loc[i, 'Comment Id'] in comment_dict:
#                 # Append the reply to the existing comment
#                 comment_dict[data.loc[i, 'Comment Id']].append(str(data.loc[i+1, 'Comment Text']))  # Convert to string
#             else:
#                 # Create a new entry for the comment in the dictionary
#                 comment_dict[data.loc[i, 'Comment Id']] = [str(data.loc[i+1, 'Comment Text'])]  # Convert to string

#     # Create a new DataFrame from the dictionary
#     modified_data = pd.DataFrame(columns=data.columns)

#     for comment_id, replies in comment_dict.items():
#         modified_data = pd.concat([modified_data, data[data['Comment Id'] == comment_id]])
#         # Set the replies in the 'reply' column for each comment
#         modified_data.loc[modified_data['Comment Id'] == comment_id, 'reply'] = '; '.join(replies)

#     # Save the modified DataFrame back to a new CSV file
#     modified_data.to_csv(output_csv_file_path, index=False)

# if __name__ == "__main__":
#     input_folder = "reverse_file"    # Replace with the path to the folder containing input CSV files
#     output_folder = "final_csv"  # Replace with the path where you want to save the modified CSV files

#     try:
#         # Create the output folder if it doesn't exist
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         for filename in os.listdir(input_folder):
#             if filename.endswith('.csv'):
#                 input_csv_file_path = os.path.join(input_folder, filename)
#                 output_csv_file_path = os.path.join(output_folder, filename)

#                 try:
#                     process_csv(input_csv_file_path, output_csv_file_path)
#                     print(f"CSV file processed and modified for {filename}.")
#                 except Exception as e:
#                     print(f"An error occurred while processing {filename}: {e}")
#     except FileNotFoundError:
#         print("Folder not found. Please check the folder path.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# ========== sort out comment and reply code end====

# ============ convert final csv file into excel ===


# csv_folder = 'final_csv'    # Replace with the path to the folder containing CSV files
# xlsx_folder = 'final_xlsx'  # Replace with the path where you want to save XLSX files

# # Create the XLSX folder if it doesn't exist
# if not os.path.exists(xlsx_folder):
#     os.makedirs(xlsx_folder)

# # Loop through each CSV file in the folder
# for filename in os.listdir(csv_folder):
#     if filename.endswith('.csv'):
#         csv_path = os.path.join(csv_folder, filename)
#         xlsx_filename = os.path.splitext(filename)[0] + '.xlsx'
#         xlsx_path = os.path.join(xlsx_folder, xlsx_filename)

#         # Read CSV file using pandas
#         df = pd.read_csv(csv_path)

#         # Save DataFrame as XLSX file
#         df.to_excel(xlsx_path, index=False)

# print("Conversion completed.")




# ========== covert into csv to xlsx code end ==========
