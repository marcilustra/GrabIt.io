import re
import shutil
from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime
import time as t

# Prompt user for folder name
folder_name = input("Enter folder name: ")
# Prompt user for textfile name, including the extension
file_name = input("File name including the .txt extension\n")

# Create folder
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder {folder_name}")

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

def download_jpg_links(url, filename):
    jpg_links = get_jpg_links(url)
    with open(filename, "w") as f:
        f.write("\n".join(jpg_links))
    print(f"Saved {len(jpg_links)} .jpg links to {filename}")


def crawl_gallery(input_file):
    with open(input_file, "r") as f:
        gallery_links = f.readlines()

    # folder_name = os.path.splitext(input_file)[0]
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Created folder {folder_name}")

    for link in gallery_links:
        gallery_url = link.strip()
        print(f"Processing {gallery_url}")
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(folder_name, f"{os.path.basename(gallery_url)}_{now}.txt")

        # Wait for 1 second before downloading the links
        wait = t.sleep
        wait(1)

        download_jpg_links(gallery_url, output_file)
        os.rename(output_file, os.path.join(folder_name, os.path.basename(output_file)))

 # Batch copy all the text files into one batch file
    batch_file_name = os.path.join(folder_name, "all_links.txt")
    with open(batch_file_name, "w") as f:
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                if file.endswith(".txt") and file != "all_links.txt":
                    with open(os.path.join(root, file), "r") as f2:
                        links = f2.readlines()
                        for link in links:
                            f.write(link.strip() + "\n")
                    print(f"Copied links from {file} to {batch_file_name}")

    print(f"All links have been batched into {batch_file_name}")

    # Move the input file to a _complete folder
    complete_folder_name = "_complete"
    if not os.path.exists(complete_folder_name):
        os.mkdir(complete_folder_name)
        print(f"Created folder {complete_folder_name}")
    shutil.move(input_file, os.path.join(complete_folder_name, os.path.basename(input_file)))
    print(f"Moved {input_file} to {complete_folder_name}")

crawl_gallery(file_name)
