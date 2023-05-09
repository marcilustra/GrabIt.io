import os
import requests

# Get the path of the parent directory of the script
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Create a folder to save the downloaded images in
images_folder = os.path.join(parent_dir, os.path.basename(parent_dir))
os.makedirs(images_folder, exist_ok=True)

# Read the links from a text file
links_file = "all_links.txt"
with open(links_file, "r") as f:
    links = [line.strip() for line in f.readlines()]

# Download and save the images
for i, link in enumerate(links):
    try:
        response = requests.get(link)
        if response.status_code == 200 and response.headers.get("content-type") == "image/jpeg":
            filename = os.path.join(images_folder, f"{i}.jpg")
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Saved image {i}: {filename}")
        else:
            print(f"Skipped link {i}: {link}")
    except Exception as e:
        print(f"Error downloading link {i}: {link}")
        print(e)

def move_txt_files_to_links_folder():
    # Create the 'links' directory if it doesn't exist
    links_dir = os.path.join(os.getcwd(), 'links')
    os.makedirs(links_dir, exist_ok=True)

    # Move all .txt files in the current directory to the 'links' directory
    for file in os.listdir(os.getcwd()):
        if file.endswith('.txt'):
            source_file = os.path.join(os.getcwd(), file)
            dest_file = os.path.join(links_dir, file)
            os.rename(source_file, dest_file)
            print(f'Moved file {file} to {dest_file}')
