# Web Scraper
Web scraping of Autonomous vehicle companies job career
## Installation
### Installing web scraping frame work
```python
pip install BeautifulSoup4
pip install selenium
```
### Anaconda and Jupyter Notebook(Windows)
1. Download Anaconda from below link
<br>[Anaconda](https://www.anaconda.com/products/individual)
2. Open "Anaconda Prompt"
3. Enter below in the prompt to open Jupyter Notebook
```bash
jupyter notebook
```
## Usage
```python
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
```
