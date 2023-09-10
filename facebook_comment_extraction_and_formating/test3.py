
# import pandas as pd
# import csv

# Read the CSV data into a pandas DataFrame
# data = pd.read_csv('sorted_csv_file.csv')

# # Iterate through the DataFrame
# for i in range(len(data)):
#     # Check if the "Comment Count" is greater than 0
#     if data.loc[i, 'Comment Count'] > 0:
#         # Take the "Comment Text" from the next row and put it in the "reply" column
#         data.loc[i, 'reply'] = data.loc[i+1, 'Comment Text']

# # Save the modified DataFrame back to a new CSV file
# data.to_csv('final_csv_file/modified_csv_file.csv', index=False)



# import pandas as pd

# # Read the CSV data into a pandas DataFrame
# data = pd.read_csv('main.csv')

# # Create a new DataFrame to store the modified data
# modified_data = pd.DataFrame(columns=data.columns)
# data_len = len(data)
# # Iterate through the DataFrame
# for i in range(480):
#     # Check if the "Comment Count" is greater than 0
#     if data.loc[i, 'Comment Count'] > 0:
#         # Copy the current row to the modified DataFrame
#         modified_data = pd.concat([modified_data, data.loc[i:i]])
#         # Take the "Comment Text" from the next row and put it in the "reply" column
#         modified_data.loc[modified_data.index[-1], 'reply'] = data.loc[i+1, 'Comment Text']
#     else:
#         # If "Comment Count" is 0, skip the current row
#         continue

# # Save the modified DataFrame back to a new CSV file
# modified_data.to_csv('modified_csv_file.csv', index=False)

# import pandas as pd

# # Read the CSV data into a pandas DataFrame
# data = pd.read_csv('main.csv')

# # Create a new DataFrame to store the modified data
# modified_data = pd.DataFrame(columns=data.columns)
# data_len = len(data)
# # Initialize an index counter for the modified DataFrame
# index_counter = 0

# # Iterate through the DataFrame
# for i in range(data_len):
#     # Check if the "Comment Count" is greater than 0
#     if data.loc[i, 'Comment Count'] > 0:
#         # Copy the current row to the modified DataFrame
#         modified_data.loc[index_counter] = data.loc[i]
#         index_counter += 1
#         # Take the "Comment Text" from the next row and put it in the "reply" column
#         if i < data_len - 1:
#             modified_data.loc[index_counter - 1, 'reply'] = data.loc[i+1, 'Comment Text']
#     else:
#         # If "Comment Count" is 0, skip the current row
#         continue

# # Save the modified DataFrame back to a new CSV file
# modified_data.to_csv('modified_csv_file.csv', index=False)




# ================== this is the final main code =================


import pandas as pd

# Read the CSV data into a pandas DataFrame
data = pd.read_csv('sorted_csv_file.csv')


# Create a dictionary to store comments and their replies
comment_dict = {}

# Iterate through the DataFrame (excluding the last row)
for i in range(len(data) - 1):
    # Check if the "Comment Count" is greater than 0
    if data.loc[i, 'Comment Count'] > 0:
        # Check if the comment already exists in the dictionary
        if data.loc[i, 'Comment Id'] in comment_dict:
            # Append the reply to the existing comment
            comment_dict[data.loc[i, 'Comment Id']].append(str(data.loc[i+1, 'Comment Text']))  # Convert to string
        else:
            # Create a new entry for the comment in the dictionary
            comment_dict[data.loc[i, 'Comment Id']] = [str(data.loc[i+1, 'Comment Text'])]  # Convert to string

# Create a new DataFrame from the dictionary
modified_data = pd.DataFrame(columns=data.columns)

for comment_id, replies in comment_dict.items():
    modified_data = pd.concat([modified_data, data[data['Comment Id'] == comment_id]])
    # Set the replies in the 'reply' column for each comment
    modified_data.loc[modified_data['Comment Id'] == comment_id, 'reply'] = '; '.join(replies)

# Save the modified DataFrame back to a new CSV file
modified_data.to_csv('final_csv_file/modified_csv_file3.csv', index=False)







