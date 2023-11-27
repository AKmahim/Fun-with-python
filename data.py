# ========================= convert text data into json data =============

# import json

# # Initialize an empty list to store product dictionaries
# products = []

# # Read data from the file
# with open('data.txt', 'r', encoding='utf-8') as file:
#     data = file.read()

# # Split the data into individual products using double newline as a separator
# product_data = data.strip().split('\n\n')

# # Process each product data to create a product dictionary
# for product_info in product_data:
#     parts = product_info.split('\n')
#     product = {
#         "product_name": parts[0],
#         "product_image": parts[1],
#         "brand": parts[2],
#         "types": parts[3],
#         "price": parts[4],
#         "short_description": parts[5],
#         "rating": parts[6]
#     }
#     products.append(product)

# # Convert the list of product dictionaries to JSON
# json_data = json.dumps(products, indent=4, ensure_ascii=False)

# # Save the JSON data to a file
# with open('symphony.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(json_data)

# print("JSON data has been successfully created and saved to 'products.json'.")







# ====================== web crawling ================
# import requests
# from bs4 import BeautifulSoup
# import json

# # Initialize an empty list to store the extracted data
# all_data = []

# # Read the list of URLs from the data.txt file
# with open('data.txt', 'r') as file:
#     urls = file.read().splitlines()

# # Iterate through each URL
# for url in urls:
#     url = url.strip()  # Remove leading/trailing spaces
#     if not url:
#         continue  # Skip empty lines

#     try:
#         # Send an HTTP GET request to the URL
#         response = requests.get(url)
#         response.raise_for_status()  # Check for HTTP request errors

#         # Parse the HTML content of the page using BeautifulSoup
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find all tables on the page
#         tables = soup.find_all('table')

#         # Check if there are at least two tables on the page
#         if len(tables) >= 2:
#             # Get the second table (index 1) and extract its data
#             second_table = tables[1]
#             table_data = {}
#             for row in second_table.find_all('tr'):
#                 columns = row.find_all('td')
#                 if len(columns) == 2:
#                     key = columns[0].get_text().strip()
#                     value = columns[1].get_text().strip()
#                     table_data[key] = value

#             # Add the extracted data to the list
#             all_data.append(table_data)
#         else:
#             print(f"There are not enough tables on the page to extract data for {url}")
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to retrieve the page for {url}: {str(e)}")

# # Convert the list of data to JSON format
# json_data = json.dumps(all_data, indent=4, ensure_ascii=False)

# # Save the JSON data to a file
# with open('details.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(json_data)

# print("JSON data has been successfully created and saved to 'details.json'.")


# ================= web crawling 2 =========================
# import requests
# from bs4 import BeautifulSoup
# import json

# # Function to scrape data from a URL
# def scrape_data(url):
#     # Send an HTTP GET request to the URL
#     response = requests.get(url)

#     # Create a dictionary to store the extracted data
#     result = {}
#     base_url = "https://www.mobiledokan.com"

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content of the page
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find all the figure tags with class 'size-full'
#         figure_tags = soup.find_all('figure', class_=['size-full', 'size-large'])

#         # Extract and store the image sources in the result dictionary
#         image_sources = []
#         for figure in figure_tags:
#             img_tag = figure.find('img')
#             if img_tag:
#                 img_src = img_tag['data-src']
#                 image_sources.append( base_url+img_src)

#         # Find the "Highlights" header
#         highlights_header = soup.find('h3', text='Highlights')

#         if highlights_header:
#             # Find the next three <p> tags after the "Highlights" header
#             p_tags = highlights_header.find_all_next('p', limit=3)

#             # Extract and store the content of the <p> tags in the result dictionary
#             paragraph_texts = [p_tag.get_text() for p_tag in p_tags]

#         # Store the image sources and details in the result dictionary
#         result["image1"] = image_sources[0] if len(image_sources) > 0 else ""
#         result["image2"] = image_sources[1] if len(image_sources) > 1 else ""
#         result["image3"] = image_sources[2] if len(image_sources) > 2 else ""
#         result["details"] = " ".join(paragraph_texts)

#         return result

#     else:
#         print(f"Failed to retrieve the webpage at {url}. Status code: {response.status_code}")
#         return None

# # Read the list of URLs from the 'data.txt' file
# with open('data.txt', 'r') as file:
#     urls = file.read().splitlines()

# # Create a list to store the scraped data
# scraped_data = []

# # Iterate through the URLs and scrape data
# for url in urls:
#     print(f"Scraping data from {url}")
#     data = scrape_data(url)
#     if data:
#         scraped_data.append(data)

# # Save the scraped data to a single JSON file
# with open('phone2.json', 'w') as json_file:
#     json.dump(scraped_data, json_file, indent=4)

# print("Scraped data saved to 'phone2.json'")


# {
#     "image1":"https://www.mobiledokan.com/wp-content/uploads/2023/09/Xiaomi-13-Lite.jpg",
#     "image2":"https://www.mobiledokan.com/wp-content/uploads/2023/09/Xiaomi-13-Lite-blue.webp",
#     "image3": "https://www.mobiledokan.com/wp-content/uploads/2023/09/Xiaomi-13-Lite-colors.webp",
#     "details": "Xiaomi 13 Lite is the Lite version of Xiaomi 13. Lite usually means with lower price and configuration. The main highlight of this gadget is its Dual 32+8 MP front camera which is rare these days. The main 32 MP lens captures 100˚ photos which makes it an ultrawide lens. Another great thing is that it charges fully in a maximum of 40 minutes although the battery is 4500 mAh and not a typical 5000 mAh one. The AMOLED display is pleasing for the eyes with 68B colors, Dolby Vision, and HDR10+ features.The 4 nm Snapdragon 7 Gen 1 chipset from Qualcomm is a good performance and gaming chipset at this price point. There is also an optical in-display fingerprint sensor. The 13 Lite from Xiaomi is a 5 G-supported smartphone."
# }

# ==================================== merge 2 file ===========================
import json

# Load data from "phone.json" and "phone2.json"
with open("phone.json", "r") as file1, open("phone2.json", "r") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# Merge the data into a single list
merged_data = []

for entry1, entry2 in zip(data1, data2):
    # Combine data from both files into a single dictionary
    merged_entry = {
        "product_name": entry1["product_name"],
        "product_image": entry1["product_image"],
        "brand": entry1["brand"],
        "types": entry1["types"],
        "price": entry1["price"],
        "short_description": entry1["short_description"],
        "rating": entry1["rating"],
        "image1": entry2["image1"],
        "image2": entry2["image2"],
        "image3": entry2["image3"],
        "details": entry2["details"]
    }
    merged_data.append(merged_entry)

# Save the merged data to "phone3.json"
with open("phone3.json", "w") as output_file:
    json.dump(merged_data, output_file, indent=4)

print("Merged data saved to 'phone3.json'")
