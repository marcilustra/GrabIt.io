from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import subprocess

# Define the webpage URL
url = input("Enter the website URL: ")
num_links = int(input("Enter the number of links to scrape: "))
margin = int(input("Margin of error?:"))
scrolls = int(input("Scrolls incase margin is a miss"))

#Options
option = Options()

#Define Firefox Profile
option.add_argument('-headless')
option.add_argument("--private-window")
driver = webdriver.Firefox(options=option)

# Set up the Selenium driver
driver = webdriver.Firefox()  # or webdriver.Firefox() or other browser driver
driver.get(url)

# Wait for the page to load completely
time.sleep(5)

# Scroll down the page until the required number of links are scraped
links = set()
while len(links) < num_links and scrolls > 0:
    num_current_links = len(links)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    scrolls -= 1
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'https://www.yourwebsitehere.com/...' in href:
            links.add(href)
    
    # Print the number of links found so far
    print("Links found:", len(links))
    if num_current_links >= num_links - margin or num_current_links == num_links:
        break

# Save the links to a text file
with open('gallery_links.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')
list_length = len(links)
# Print the saved file location
print(f"{list_length} unique links saved to gallery_links.txt")

# Quit the driver
driver.quit()
