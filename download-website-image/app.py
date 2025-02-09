import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_images(url, folder="images"):
    # Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Get page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve URL: {url}")
        return
    
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all image tags
    img_tags = soup.find_all("img")
    if not img_tags:
        print("No images found on the page.")
        return
    
    for img in img_tags:
        img_url = img.get("src")
        if not img_url:
            continue
        
        # Convert relative URLs to absolute
        img_url = urljoin(url, img_url)
        
        # Get image filename
        parsed_url = urlparse(img_url)
        img_name = os.path.basename(parsed_url.path)

        if not img_name:
            continue
        
        # Download image
        img_data = requests.get(img_url).content
        img_path = os.path.join(folder, img_name)

        # Save image
        with open(img_path, "wb") as f:
            f.write(img_data)
        
        print(f"Downloaded: {img_name}")

# Example usage
website_url = "https://themeholy.com/html/agenxe/demo/index.html"  # Replace with your target URL
download_images(website_url)
