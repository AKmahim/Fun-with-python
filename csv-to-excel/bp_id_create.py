import pandas as pd
import requests
import time

# Read the Excel file into a pandas DataFrame
excel_file = "BP.xlsx"
df = pd.read_excel(excel_file)

# API endpoint
api_url = "http://127.0.0.1:8000/api/register"

# Rate limiting parameters
users_per_minute = 40
time_interval = 60 / users_per_minute

# Iterate over rows of the DataFrame
for index, row in df.iterrows():
    # Extract data from the current row
    name = row['Name']
    print(name)
    phone_number = str(row['Phone'])  # Convert to string if needed
    bp_id = row['bp_id']
    password = row['password']
    area = row['Area']  # Assuming 'Area' maps to 'working_district'

    # Adding '0' prefix to phone number if it's missing
    if not phone_number.startswith('0'):
        phone_number = '0' + phone_number


    # Form data for the POST request
    form_data = {
        'name': name,
        'phone_number': phone_number,
        'bp_id': bp_id,
        'password': password,
        'working_district': area  # Assuming 'Area' maps to 'working_district'
    }

    # Send POST request to the API
    response = requests.post(api_url, data=form_data)

    # Check response status
    if response.status_code == 200:
        print(f"User {name}, {bp_id} created successfully.")
    else:
        print(f"Failed to create user {name},{bp_id}. Status code: {response.status_code}")
        print(f"error: {response.error}")

    # Rate limiting: wait for the specified time interval before proceeding to the next iteration
    time.sleep(time_interval)





# ==================================== convert bp excel file into a csv file ========================== 
# import pandas as pd

# def excel_to_csv(input_file, output_file):
#     try:
#         # Read Excel file
#         df = pd.read_excel(input_file)
        
#         # Write DataFrame to CSV
#         df.to_csv(output_file, index=False)
        
#         print(f"Excel file '{input_file}' successfully converted to CSV file '{output_file}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_file = 'BP.xlsx'  # Replace 'input.xlsx' with your Excel file name
# output_file = 'BP.csv'  # Replace 'output.csv' with your desired CSV file name

# excel_to_csv(input_file, output_file)
