# GrabIt.io
This is a small Python script to automate image reference gathering from Online Galleries. Personal use. Might make it in other languages.
Uses, BeautifulSoup4 to achieve the desired effect.

## Problem.
Trying to get multiple images from a gallery page without having to open a new tab and right-click -> Save Image for each file.

## How it addresses problem.
The script provided will work for .jpg file links but can be modified to search for png links.
  - The linkgrabber.py script saves (to a txt file) links from a page that contains the .jpg links
  - The crawlgall.py script gets the links associated with jpg files, downloads them and saves them to a txt file based on the soupit.py script
  - The download.py downloads the links saved by crawlgall in all_links.txt

### How to Use
- Use linkgrabber.py to collect page links to galleries.
  -   Specify the number of links you want to grab and how far down you want to scroll.
- Then use crawlgall.py to grab the links to the jpgs and save them by datetime stamp filename to a folder of your choice.
- The links will batch into one file 'all_links.txt'.
- Use download.py to get them or better yet copy and paste into IDM or your preferred download manager.

Must have BS4 installed via Pip.
[Guide on how to install packages using pip](https://packaging.python.org/en/latest/tutorials/installing-packages/)
