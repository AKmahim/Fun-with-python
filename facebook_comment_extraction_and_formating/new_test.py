


# ================ this is for sorting by mention system ====
# import pandas as pd

# # Read input data from CSV file
# input_csv_file_path = '8.csv'  # Replace with your CSV file path
# df = pd.read_csv(input_csv_file_path)

# # Filter rows where the Username is mentioned in the reply
# def check_mention(row):
#     if pd.isna(row['reply']):  # Check for NaN values
#         return False
#     return row['Username'] in row['reply']

# df['mentioned'] = df.apply(check_mention, axis=1)
# mentioned_rows = df[df['mentioned']]

# # Create a new DataFrame with just the relevant columns
# new_df = mentioned_rows[["User Id", "Username", "Permalink Url", "Comment Text", "reply"]]

# # Define the new XLSX file path
# output_xlsx_file_path = 'mentioned_replies_8.xlsx'

# # Save the new DataFrame to a new XLSX file
# new_df.to_excel(output_xlsx_file_path, index=False)

# print(f"New XLSX file '{output_xlsx_file_path}' with mentioned replies has been created.")








# ================= find out mention ===============
# import pandas as pd

# # Load the XLSX file into a DataFrame
# df = pd.read_excel("remove_duplicate.xlsx")

# # Iterate through the rows and update reply if Username is found in any reply row
# for i in range(len(df)):
#     if pd.notna(df.loc[i, 'Username']):
#         for j in range(i + 1, len(df)):
#             if pd.notna(df.loc[j, 'reply']) and df.loc[i, 'Username'] in df.loc[j, 'reply']:
#                 df.loc[j, 'reply'] = df.loc[i, 'reply']
#                 break

# # Save the modified DataFrame to an XLSX file
# df.to_excel("mention_finding.xlsx", index=False)

# ==========================================================================final ============================================


# ================= convert xlsx file to csv ==========
import pandas as pd

# Load the Excel file
xlsx_file_path = 'new_file/13 (1).xlsx'
df = pd.read_excel(xlsx_file_path)

# Define the CSV file path
csv_file_path = 'new_file/text.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"XLSX file '{xlsx_file_path}' has been successfully converted to CSV file '{csv_file_path}'.")



# ================= remove reply that is available in next comment * this is remove file system 2
# import pandas as pd

# # Load the CSV file into a DataFrame
# df = pd.read_csv("new_file/13.csv")

# # Iterate through the rows and update reply if reply is present in the next row's Comment Text
# for i in range(len(df) - 1):
#     if pd.notna(df.loc[i, 'reply']) and pd.notna(df.loc[i + 1, 'Comment Text']):
#         if df.loc[i, 'reply'] in df.loc[i + 1, 'Comment Text']:
#             df.loc[i, 'reply'] = ''

# # Save the modified DataFrame to an XLSX file
# df.to_excel("new_file/12_rem2.xlsx", index=False)


# =========================== find mention and stay not mention ============

# import pandas as pd

# # Read input data from CSV file
# input_csv_file_path = 'new_file/13.csv'  # Replace with your CSV file path
# df = pd.read_csv(input_csv_file_path)

# # Filter rows where the Username is mentioned in the reply
# def check_mention(row):
#     if pd.isna(row['reply']):  # Check for NaN values
#         return False
#     return row['Username'] in row['reply']

# df['mentioned'] = df.apply(check_mention, axis=1)

# # Define the new XLSX file path
# output_xlsx_file_path = 'new_file/17_men.xlsx'

# # Save the DataFrame with all rows (mentioned and not mentioned) to a new XLSX file
# df.to_excel(output_xlsx_file_path, index=False)

# print(f"New XLSX file '{output_xlsx_file_path}' has been created.")


# ======================== remove that is not mention and left empty =====


# import pandas as pd

# # Read input data from XLSX file
# input_xlsx_file_path = 'new_file/17_men.xlsx'  # Replace with your XLSX file path
# df = pd.read_excel(input_xlsx_file_path)

# # Filter rows where the Username is mentioned in the reply
# def check_mention(row):
#     if pd.isna(row['reply']):  # Check for NaN values
#         return False
#     return row['Username'] in row['reply']

# df['mentioned'] = df.apply(check_mention, axis=1)

# # Remove 'reply' content where no one is mentioned
# df.loc[~df['mentioned'], 'reply'] = ''

# # Remove the 'mentioned' column as it's not needed anymore
# df.drop(columns=['mentioned'], inplace=True)

# # Define the new XLSX file path
# output_xlsx_file_path = 'new_file/17_rem.xlsx'

# # Save the modified DataFrame to a new XLSX file
# df.to_excel(output_xlsx_file_path, index=False)

# print(f"New XLSX file '{output_xlsx_file_path}' has been created.")




# ========================================= replace price comment by price reply ===========
# import pandas as pd

# # Read input data from XLSX file
# input_xlsx_file_path = 'new_file/17_rem.xlsx'  # Replace with your XLSX file path
# df = pd.read_excel(input_xlsx_file_path)

# # Define the desired keywords
# desired_keywords = "আমি নিতে চাই,দাম,প্রাইজ প্লিজ,?,Prize,prize,Amar lagbe, purchase,I want to buy,price,Interested,আমি নিতে আগ্রহী,Pp,pp,pp?,Price,Price?,Cash price koto?,দাম কত,Want to purchase.,I need,এইটার দাম কত টাকা?,Vai dam koto,dam koto,Total price please,কিভাবে কি"
# # reply_ans = "পিউরইট সম্পর্কে আগ্রহ প্রকাশ করার জন্য ধন্যবাদ। প্রিয় গ্রাহক, আপনি যদি CITY AMEX/SCB/Brac Bank/EBL/UCB/DBBL/NRB/NCC/NRBC/Trust Bank-এর ডেবিট অথবা ক্রেডিট কার্ড গ্রাহক হন, তাহলে আপনি এখন Ultima RO+UV+MF ডিভাইসটি ৩২,৫০০/- টাকার পরিবর্তে পাচ্ছেন ৩০,৫০০/- টাকায়, Marvella Slim RO+UV+MF ডিভাইসটি ২৫,৫০০/- টাকার পরিবর্তে পাচ্ছেন ২৪,০০০/- টাকায়, এবং Classic Mineral RO+MF ডিভাইসটি ১৯,৫০০/- টাকার পরিবর্তে এখন পাচ্ছেন ১৮,০০০/- টাকায়। এছাড়াও সর্বোচ্চ ১২ মাসের 0% EMI সুবিধাও পাচ্ছেন। Pureit Ultima RO+UV+MF ডিভাইসটির স্টোরেজ ট্যাংক ১০ লিটার, Marvella Slim RO+UV+MF ডিভাইসটির স্টোরেজ ট্যাংক ৮ লিটার এবং Classic Mineral RO+MF ডিভাইসটির স্টোরেজ ট্যাংক ৬ লিটার।  বিস্তারিত জানতে অনুগ্রহ করে আপনার নাম্বারটি আমাদের ইনবক্সে শেয়ার করুন যাতে আমাদের প্রতিনিধি আপনাকে এ বিষয়ে সহযোগিতা করতে পারে অথবা আমাদের কেয়ারলাইন নাম্বার ১৬৬২৭ (সকাল ৮টা- রাত ১২টা) - এ কল করতে পারছেন। এছাড়াও বিস্তারিত জানতে আমাদের Website ভিজিট করুন: https://bd.pureitwater.com ধন্যবাদ।"
# reply_ans = "পিওরইট সম্পর্কে আগ্রহ প্রকাশ করার জন্য ধন্যবাদ। প্রিয় গ্রাহক, আমাদের Classic 23L ডিভাইসটির মূল্য ৪,৯৯৯ টাকা। বিস্তারিত জানতে অনুগ্রহ করে আপনার নাম্বারটি আমাদের ইনবক্সে শেয়ার করুন যাতে আমাদের প্রতিনিধি আপনাকে এ বিষয়ে সহযোগিতা করতে পারে অথবা আমাদের কেয়ারলাইন নাম্বার ১৬৬২৭ (সকাল ৮টা-রাত ১২টা) -এ কল করতে পারছেন। এছাড়াও বিস্তারিত জানতে আমাদের Website ভিজিট করুন: https://bd.pureitwater.com ধন্যবাদ।"
# # Filter rows where the reply is empty and Comment Text contains desired keywords
# def fill_empty_reply(row):
#     if pd.isna(row['reply']) and any(keyword in row['Comment Text'] for keyword in desired_keywords.split(',')):
#         return f"{row['Username']} {reply_ans}"
#     return row['reply']

# df['reply'] = df.apply(fill_empty_reply, axis=1)

# # Define the new XLSX file path
# output_xlsx_file_path = 'new_file/17_final.xlsx'

# # Save the modified DataFrame to a new XLSX file
# df.to_excel(output_xlsx_file_path, index=False)

# print(f"New XLSX file '{output_xlsx_file_path}' has been created.")
