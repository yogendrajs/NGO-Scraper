# NGO-Scraper

In this project, I have scraped the data of all the NGOs that donate funds certified by **GiveIndia** at `https://www.giveindia.org/certified-indian-ngos` according to their Location, and I have stored all the data in the `ngo_scraper.json` file.

## Requirements

### BeautifulSoup

Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. If you're using Linux based OS, you can install BeautifulSoup using following command in terminal.

Here, pip is a package-management system used to install and manage software packages written in Python
```sudo apt-get update && sudo apt-get install python3-pip (Python3).
pip3 install beautifulsoup4
```

## Instructions to run the code

Any version of Python3 should be installed on your Linux-based computer. Navigate to your directory where your `ngo_scraper.py` file is located. You can run the code using the following command on your terminal.

`python3 ngo_scraper.py`
