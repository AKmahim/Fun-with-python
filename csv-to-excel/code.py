# import pandas as pd

# # Read the CSV file with the correct delimiter
# df = pd.read_csv('contestants.csv', sep=';')

# # Add prefix to the 'alpona' column
# df['alpona'] = 'https://share-your-alpona.alponayboishakh.com/' + df['alpona']

# # Write the modified data to an Excel file
# df.to_excel('contestant.xlsx', index=False)



# import pandas as pd

# # Read the Excel file
# df = pd.read_excel('eid_number.xlsx')

# # Function to add prefix based on number format
# def add_prefix(number):
#     numbers = str(number).split()
#     modified_numbers = []
#     for num in numbers:
#         num_str = num.strip()
#         if len(num_str) < 13:
#             if num_str.startswith('0'):
#                 modified_numbers.append('88' + num_str[1:])
#             else:
#                 modified_numbers.append('880' + num_str)
#         else:
#             modified_numbers.append(num_str)
#     return ' '.join(modified_numbers)

# # Apply the function to the 'Number' column
# df['Number'] = df['Number'].apply(add_prefix)

# # Write the modified numbers to a text file
# with open('numbers_with_prefix.txt', 'w') as f:
#     for number in df['Number']:
#         f.write("%s\n" % number)



# import pandas as pd

# # Read the Excel file
# df = pd.read_excel('eid_number.xlsx')

# # Open a text file to write the numbers
# with open('numbers.txt', 'w') as file:
#     # Iterate through each row in the DataFrame
#     for index, row in df.iterrows():
#         # Convert the 'Number' field to string
#         number_field = str(row['Number'])
#         # Split the numbers if there are multiple numbers in the field
#         numbers = number_field.split(',')
#         # Write each number to the text file
#         for number in numbers:
#             # Remove any leading or trailing whitespaces
#             number = number.strip()
#             # Write the number to the text file
#             file.write(number + '\n')



# Open the numbers.txt file for reading
with open('numbers.txt', 'r') as file:
    # Read all lines from the file
    numbers = file.readlines()

# Open the numbers.txt file for writing
with open('formatted_numbers.txt', 'w') as file:
    # Iterate through each number
    for number in numbers:
        # Remove leading and trailing whitespaces
        number = number.strip()
        # Check if the number starts with '0'
        if number.startswith('0'):
            # Add '88' prefix
            formatted_number = '88' + number
        else:
            # Add '880' prefix
            formatted_number = '880' + number
        # Write the formatted number to the file
        file.write(formatted_number + '\n')
