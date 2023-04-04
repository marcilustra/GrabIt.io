import requests
imnport os
import time as t
from datetime import datetime
from bs4 import BeautifulSoup

def get_jpg_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    return [link.get("href") for link in links if link.get("href").lower().endswith(".jpg")]

def get_gallery_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    return [link.get("href") for link in links]
    
# This function based on the soupit cript will save url links ending with .jpg 
# from the previous functions to a txt file that will then be used to store the links.

def download_jpg_links(url, filename):
    jpg_links = get_jpg_links(url)
    with open(filename, "w") as f:
        f.write("\n".join(jpg_links))
    print(f"Saved {len(jpg_links)} .jpg links to {filename}")

def crawl_gallery(input_file):
    with open(input_file, "r") as f:
        gallery_links = f.readlines()

    for link in gallery_links:
        gallery_url = link.strip()
        print(f"Processing {gallery_url}")
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{os.path.basename(gallery_url)}_{now}.txt"

        # Wait for 1 second before downloading the links
        wait = t.sleep
        wait(1)


        download_jpg_links(gallery_url, output_file)
        
# Example usage:
crawl_gallery("links_file.txt")
