import requests
from bs4 import BeautifulSoup
import os

# Replace this with your website link
website_link = "https://www.worldometers.info/geography/flags-of-the-world/"

# Create a directory to store the downloaded images
os.makedirs("flags_images", exist_ok=True)

# Get the HTML content of the website
response = requests.get(website_link)
response.raise_for_status()  # Check for HTTP errors
soup = BeautifulSoup(response.content, "html.parser")

# Find all image tags and their corresponding captions
image_tags = soup.find_all("img")

for image_tag in image_tags:
    image_url = image_tag.get("src")

    # Find the div with bold text next to the image tag
    name_div = image_tag.find_next_sibling("div", style="font-weight:bold") 
    if name_div:
  		# Extract the text from the div
        image_name = name_div.text.strip()
    else:
 		# Use filename from URL if no div is found
        image_name = os.path.basename(image_url) 

    # Download the image
    image_data = requests.get(image_url).content

    # Save the image with the renamed filename
    with open(f"flags_images/{image_name}", "wb") as f:
        f.write(image_data)

print("Images downloaded successfully!")

