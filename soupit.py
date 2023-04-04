from bs4 import BeautifulSoup
import requests

url = "https://www.examplelink.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("a")

jpg_links = [link.get("href") for link in links if link.get("href").lower().endswith(".jpg")]

with open("jpg_links.txt", "w") as f:
    f.write("\n".join(jpg_links))

print(f"Saved {len(jpg_links)} .jpg links to jpg_links.txt")
