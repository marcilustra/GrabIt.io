# ImageSnatch
This is a small Python script to automate image reference gathering from Online Galleries. Personal use. Might make it in other languages.
Uses, BeautifulSoup4 to achieve the desired effect.

## Problem.
Trying to get multiple images from a gallery page without having to open a new tab and right-click -> Save Image for each file.

## How it addresses problem.
Python being an interpreted language allows you to modify the code to suit your needs. Thus the script provided will work for .jpg file links.
  - The soupit.py script saves (to a txt file) links from a page that contain the .jpg links
  - The crawlgall.py script gets the links associated with jpg files, downloads them and saves them to a txt file based on the soupit.py script

# How to Use
Paste the destination address of the file containing the links to the image files downloaded by the soupit script and run from Command Line.
Must have BS4 installed via Pip.
[Guide on how to install packages using pip](https://packaging.python.org/en/latest/tutorials/installing-packages/)
