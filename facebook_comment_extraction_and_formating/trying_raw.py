# ==================== converting from raw file =========
# import pandas as pd
# import json
# # Load the Excel file
# input_file = 'new_file/20.xlsx'
# output_file = 'new_file/20_final.xlsx'

# excel = pd.read_excel(input_file)


# def delete_items_by_value(dct, value):
#     keys_to_delete = [key for key, val in dct.items() if val == value]
    
#     for key in keys_to_delete:
#         del dct[key]
    
#     return keys_to_delete


# pureit_comments = excel[excel['Username'] == 'Pureit Bangladesh']
# # print(pureit_comments)
# # Create a dictionary for the comments
# comments_dict = {}
# for index, row in pureit_comments.iterrows():
#     comments_dict[row['Comment Text']] = row['Username']


# # # Load JSON data from the file
# # with open('new_file/pureit_comments.json', 'r', encoding='utf-8') as json_file:
# #     data = json.load(json_file)
# comment_rows = []
# for index, row in excel.iterrows():
#     main = row['Username']
#     # if(row['Username'])
#     counter = 0
#     for comment, username in comments_dict.items():

#         if(main in comment):
#             comment_rows.append({
#             'User Id': row['User Id'],
#             'Username': row['Username'],
#             'Permalink Url' : row['Permalink Url'],
#             'Comment Id': row['Comment Id'],
#             'Comment Text': row['Comment Text'],
#             'Reply Text': comment,
#             'Like Count': row['Like Count'],
            
            
#             'Date': row['Date']
#             })
#             deleted_keys = delete_items_by_value(comments_dict, comment)

    
        
        
    
    

# comment_data = pd.DataFrame(comment_rows)

# # Save the organized data to a new Excel file
# comment_data.to_excel(output_file, index=False)








# # # ==================== new try final ==========
import pandas as pd
import json
# Load the Excel file
input_file = '15.xlsx'
output_file = '15_final.xlsx'

excel = pd.read_excel(input_file)


def delete_items_by_value(dct, value):
    keys_to_delete = [key for key, val in dct.items() if val == value]
    
    for key in keys_to_delete:
        del dct[key]
    
    return keys_to_delete


pureit_comments = excel[excel['Username'] == 'Pureit Bangladesh']
# print(pureit_comments)
# Create a dictionary for the comments
comments_dict = {}
for index, row in pureit_comments.iterrows():
    comments_dict[row['Comment Text']] = row['Username']


# # Load JSON data from the file
# with open('new_file/pureit_comments.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)
comment_rows = []
for index, row in excel.iterrows():
    main = str(row['Username'])
    if (main == 'Pureit Bangladesh'):
        continue
    
    # if(row['Username'])
    comment_text = ''
    for comment, username in comments_dict.items():

        if(main in str(comment)):

            comment_text = comment
            deleted_keys = delete_items_by_value(comments_dict, comment)
            break

    comment_rows.append({
            'User Id': row['User Id'],
            'Username': row['Username'],
            'Permalink Url' : row['Permalink Url'],
            'Comment Id': row['Comment Id'],
            'Comment Text': row['Comment Text'],
            'Reply Text': comment_text,
            'Like Count': row['Like Count'],
            'Date': row['Date']
    })
    
        
        
    
    

comment_data = pd.DataFrame(comment_rows)

# Save the organized data to a new Excel file
comment_data.to_excel(output_file, index=False)








# # ============== for all file ==============
# import os
# import pandas as pd

# def delete_items_by_value(dct, value):
#     keys_to_delete = [key for key, val in dct.items() if val == value]
    
#     for key in keys_to_delete:
#         del dct[key]
    
#     return keys_to_delete

# def process_xlsx(input_file, output_file):
#     excel = pd.read_excel(input_file)

#     pureit_comments = excel[excel['Username'] == 'Pureit Bangladesh']
#     comments_dict = {}
#     for index, row in pureit_comments.iterrows():
#         comments_dict[row['Comment Text']] = row['Username']

#     comment_rows = []
#     for index, row in excel.iterrows():
#         main = str(row['Username'])
#         if main == 'Pureit Bangladesh':
#             continue
        
#         comment_text = ''
#         for comment, username in comments_dict.items():
#             if main in str(comment):
#                 comment_text = comment
#                 deleted_keys = delete_items_by_value(comments_dict, comment)
#                 break
        
#         comment_rows.append({
#             'User Id': row['User Id'],
#             'Username': row['Username'],
#             'Permalink Url' : row['Permalink Url'],
#             'Comment Id': row['Comment Id'],
#             'Comment Text': row['Comment Text'],
#             'Reply Text': comment_text,
#             'Like Count': row['Like Count'],
#             'Date': row['Date']
#         })

#     result_df = pd.DataFrame(comment_rows)
#     result_df.to_excel(output_file, index=False)
#     print(input_file)

# xlsx_directory = 'june_raw'
# output_dic = 'june_final'
# xlsx_files = [file for file in os.listdir(xlsx_directory) if file.endswith('.xlsx')]

# for xlsx_file in xlsx_files:
#     input_file = os.path.join(xlsx_directory, xlsx_file)
#     output_file = os.path.join(output_dic, xlsx_file.replace('.xlsx', '_final.xlsx'))

#     process_xlsx(input_file, output_file)
