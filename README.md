# ImageSnatch
This is a small Python script to automate image reference gathering from Online Galleries. Personal use. Might make it in other languages.
Uses, BeautifulSoup4 to achieve the desired effect.

## Problem.
Trying to get multiple images from a gallery page without having to open a new tab and right-click -> Save Image for each file.

## How it addresses problem.
The script provided will work for .jpg file links but can be modified to search for png links.
  - The soupit.py script saves (to a txt file) links from a page that contain the .jpg links
  - The crawlgall.py script gets the links associated with jpg files, downloads them and saves them to a txt file based on the soupit.py script

### How to Use
- Use linkgrabber.py to collect links from gallery page links and save them to a txt file.
- Then use crawlgall.py to grab the links to the jpgs and save them by datetime stamp filename.
- The links will batch into one file 'all_links.txt'.
- Use download.py to get them or better yet copy and paste into IDM or your preferred download manager.

Must have BS4 installed via Pip.
[Guide on how to install packages using pip](https://packaging.python.org/en/latest/tutorials/installing-packages/)
