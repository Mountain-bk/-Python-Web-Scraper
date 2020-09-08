from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# scraping tesla
def get_tesla_engineer_job_information():
    print("---Tesla Software Job Information---")
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    # fill in keyword you want to search
    keyword = 'software'
    driver.get('https://www.tesla.com/jp/careers/search#/?keyword=' + keyword + '&department=4&country=0')
    # 2 seconds to complete the load
    time.sleep(2)
    tesla_soup = BeautifulSoup(driver.page_source, 'lxml')
    job_list = tesla_soup.find('tbody', attrs={'data-reactid': ".0.0.1.0.0.1"})
    for job_title in job_list.find_all('th', {'class': 'listing-title'}):
        try:
            link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '" + job_title.text + "')]"))
            )
            link.click()
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), '" + job_title.text + "')]"))
            )
            print(title.text)
        finally:
            driver.back()

    driver.quit()

# scraping waymo
waymo_career = requests.get('https://waymo.com/joinus/').text
waymo_soup = BeautifulSoup(waymo_career, 'lxml')

def get_waymo_software_engineer_job_information():
    # Software Engineer Category
    software_engineer = waymo_soup.find('li', {'ng-if': "ctrl.categoryIsActive('Software Engineering', ['Mountain View, California, United States','New York, New York, United States','San Francisco, California, United States','Seattle, Washington, United States','Oxford, England, United Kingdom','Ann Arbor, Michigan, United States',])"})
    get_waymo_job_information(software_engineer)

def get_waymo_system_engineer_job_information():
    # Systems Engineer Category
    system_engineer = waymo_soup.find('li', {'ng-if': "ctrl.categoryIsActive('Systems Engineering', ['Mountain View, California, United States',])"})
    get_waymo_job_information(system_engineer)

def get_waymo_job_information(job_type):
    for job_link in job_type.find_all('a', {'class': 'ak-update-params'}, href=True):
        # get the specific job link page
        job_role_page = requests.get('https://waymo.com' + job_link['href']).text

        new_soup = BeautifulSoup(job_role_page, 'lxml')
        job_title = new_soup.find('div', {'class': 'career__title'}).text
        job_description = new_soup.find('div', {'class': 'career__description'}).text
        print("")
        print(job_title)
        print(job_description)
        print("")





get_waymo_software_engineer_job_information()
get_waymo_system_engineer_job_information()
get_tesla_engineer_job_information()
