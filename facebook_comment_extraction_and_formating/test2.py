
# ================ this code is for sorting csv file in reverse order 


# import csv

# def read_csv_reverse(file_path):
#     with open(file_path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         data = list(reader)
#         header = data[0]  # Extract the header row
#         reversed_data = list(reversed(data[1:]))  # Exclude the header row while reversing
#         return header, reversed_data

# def print_csv_reversed(header, data):
#     print(','.join(header))  # Print the header row first
#     for row in data:
#         print(','.join(row))  # Assumes the CSV file uses commas as the delimiter

# def write_csv_reversed(file_path, header, data):
#     with open(file_path, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(header)  # Write the header row
#         writer.writerows(data)   # Write the reversed data rows

# if __name__ == "__main__":
#     input_csv_file_path = "main.csv"
#     output_csv_file_path = "sorted_csv_file.csv"

#     try:
#         header, reversed_csv_data = read_csv_reverse(input_csv_file_path)
#         write_csv_reversed(output_csv_file_path, header, reversed_csv_data)
#         print("New CSV file with reversed data has been created.")
#     except FileNotFoundError:
#         print("File not found. Please check the file path.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
