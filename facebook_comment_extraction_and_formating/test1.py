

# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse, unquote
# from urllib.request import urlretrieve
# import time

# # URL of the website to download images from
# website_url = "https://www.unicef.org/"

# # Send a GET request to the website with user-agent header
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# }
# response = requests.get(website_url, headers=headers)
# soup = BeautifulSoup(response.content, "html.parser")

# # Create a directory to save the downloaded images
# os.makedirs("downloaded_images", exist_ok=True)

# # Find all image tags and extract their source URLs
# img_tags = soup.find_all("img")
# for img_tag in img_tags:
#     img_url = urljoin(website_url, img_tag.get("src"))
    
#     # Remove query parameters from the URL and unquote it
#     parsed_url = urlparse(img_url)
#     img_filename = unquote(os.path.basename(parsed_url.path))
    
#     # Download the image and save it in the 'downloaded_images' directory
#     img_path = os.path.join("downloaded_images", img_filename)
#     urlretrieve(img_url, img_path)
#     print(f"Downloaded: {img_url}")
    
#     # Add a delay between requests
#     time.sleep(1)

# print("All images downloaded successfully.")
 

import pyautogui as p
import time

time.sleep(5)
for i in range(5):
    p.typewrite("dekhso video?")
    p.press("enter")
