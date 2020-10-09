# Web Scraper
Web scraping of Autonomous vehicle companies job career
## Step1. Setup
### Installation
```python
pip install selenium
pip install BeautifulSoup4
```
### Download Web Driver(Chrome)
Download from below link
<br>[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

## Implementation for Web Scraping
### Step2. Import Libraries
```python
from bs4 import BeautifulSoup
import requests
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
```
### Step3. Set Driver(Selenium)
```python
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.delete_all_cookies()
```
### Step4. Put the resource you want to scrape
#### Selenium
```python
driver.get('https://XXXXXXXXXXXXX')
```
#### Beautiful Soup
```python
page = requests.get('https://XXXXXXXXX').text
soup = BeautifulSoup(page, 'lxml')
```
