from bs4 import BeautifulSoup
import requests
import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



waymo_career = requests.get('https://waymo.com/joinus/').text
waymo_soup = BeautifulSoup(waymo_career, 'lxml')
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.delete_all_cookies()

def list_to_string(lst):
    separation = ", "
    return separation.join(lst)

def extract_programming_languages(text):
    programming_language = []

    lst = re.split(r'[;,/\s]\s*', text)
    if lst.count("python") or lst.count("Python"):
        programming_language.append("Python")
    if lst.count("c") or lst.count("C"):
        programming_language.append("C")
    if lst.count("c#") or lst.count("C#"):
        programming_language.append("C#")
    if lst.count("c++") or lst.count("C++"):
        programming_language.append("C++")
    if lst.count("r") or lst.count("R"):
        programming_language.append("R")
    if lst.count("java") or lst.count("Java"):
        programming_language.append("Java")
    if lst.count("ruby") or lst.count("Ruby") :
        programming_language.append("Ruby")
    if lst.count("Javascript") or lst.count("JavaScript") or lst.count("JS"):
        programming_language.append("JavaScript")
    if lst.count("php") or lst.count("PHP"):
        programming_language.append("PHP")
    if lst.count("sql") or lst.count("SQL"):
        programming_language.append("SQL")
    if lst.count("scala") or lst.count("Scala"):
        programming_language.append("Scala")
    if lst.count("Go") or lst.count("GO"):
        programming_language.append("Go")
    if lst.count("rust") or lst.count("Rust"):
        programming_language.append("Rust")
    return programming_language

def get_waymo_software_engineer_job_information():
    print("---Waymo Software Job Information---")
    software_engineer = waymo_soup.find('li', {'ng-if': "ctrl.categoryIsActive('Software Engineering', ['Mountain View, California, United States','New York, New York, United States','San Francisco, California, United States','Seattle, Washington, United States','Oxford, England, United Kingdom','Ann Arbor, Michigan, United States',])"})
    for job_link in software_engineer.find_all('a', {'class': 'ak-update-params'}, href=True):
        # get the specific job link page
        job_role_page = requests.get('https://waymo.com' + job_link['href']).text
        url = 'https://waymo.com' + job_link['href']
        new_soup = BeautifulSoup(job_role_page, 'lxml')
        job_title = new_soup.find('div', {'class': 'career__title'}).text
        job_description = new_soup.find('div', {'class': 'career__description'}).text

        # print to terminal
        # print("")
        # print("----------" + job_title + " (Waymo) ----------")
        # print(job_description)
        # print("")

        # collect languages
        programming_language_lst = extract_programming_languages(job_description)
        #print(programming_language)

        # convert list to string
        programming_language = list_to_string(programming_language_lst)

        # input to csv file
        csv_writer.writerow({'company': 'Waymo', 'job-title': job_title, 'url': url, 'programming-languages': programming_language, 'job-description': job_description})


def get_tesla_engineer_job_information():
    print("---Tesla Software Job Information---")
    # fill in keyword you want to search
    #keyword = 'software'
    driver.get('https://www.tesla.com/jp/careers/search#/?keyword=software&department=5&country=0')
    # wait 2 seconds to complete the load
    time.sleep(2)
    tesla_soup = BeautifulSoup(driver.page_source, 'lxml')
    job_list = tesla_soup.find('tbody', attrs={'data-reactid': ".0.0.1.0.0.1"})
    for job in job_list.find_all('th', {'class': 'listing-title'}):
        try:
            link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '" + job.text + "')]"))
            )
            link.click()
            # job title
            job_title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), '" + job.text + "')]"))
            )
            # job description
            job_description = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class = 'notranslate']"))
            )
            # converting from element to string
            job_description = job_description.text
            job_title = job_title.text

            # print to terminal
            #print("")
            #print("----------" + title.text + " (Tesla) ----------")
            #print(job_description.text)
            #print("")

            # collect languages
            programming_language_lst = extract_programming_languages(job_description)

            # convert list to string
            programming_language = list_to_string(programming_language_lst)

            # retrieve url
            url = driver.current_url

            # input to csv file
            csv_writer.writerow({'company': 'Tesla', 'job-title': job_title, 'url': url, 'programming-languages': programming_language, 'job-description': job_description})
        finally:
            driver.back()

def get_gmcruise_engineer_job_information():
    print("---GM Cruise Software Job Information---")
    driver.get('https://www.getcruise.com/careers/jobs/')
    # cruise_soup = BeautifulSoup(driver.page_source, 'lxml')
    close = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'mc-closeModal')]"))
    )
    close.click()
    # find job department "Engineering - Autonomous Vehicle Software"
    vehicle_software = driver.find_element_by_xpath("//option[contains(text(), 'Engineering - Autonomous Vehicle Software')]")
    vehicle_software.click()
    url = driver.current_url
    driver.get(url)
    for link in driver.find_elements_by_xpath("//a[contains(@class, 'JobTable--job--i8IkL')]"):
        default_handle = driver.current_window_handle
        link.click()
        window = driver.window_handles
        driver.switch_to.window(window[1])
        job_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "app-title"))
        )
        job_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )

        # converting from element to string
        job_description = job_description.text
        job_title = job_title.text

        # print to terminal
        #print("")
        #print("----------" + title.text + " (GM Cruise) ----------")
        #print(job_description.text)
        #print("")

        # collect languages
        programming_language_lst = extract_programming_languages(job_description)

        # convert list to string
        programming_language = list_to_string(programming_language_lst)

        # retrieve url
        url = driver.current_url

        # input to csv file
        csv_writer.writerow({'company': 'GM-Cruise', 'job-title': job_title, 'url': url, 'programming-languages': programming_language, 'job-description': job_description})

        driver.close()
        driver.switch_to.window(default_handle)

def get_argoai_engineer_job_information():
    print("---Argo AI Software Job Information---")
    driver.get("https://www.argo.ai/join-us/#")
    cookie = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "pea_cook_btn"))
    )
    cookie.click()
    filter_btn = driver.find_element_by_xpath("//div[contains(@class, 'filter-button toggle')]")
    filter_btn.click()
    software_engineer = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Software Engineering')]"))
    )
    software_engineer.click()
    for i in range(len(driver.find_elements_by_xpath("//a[contains(@id, 'apply')]"))):
        url = driver.current_url
        # get new DOM
        driver.get(url)
        # get elements of new DOM
        links = driver.find_elements_by_xpath("//a[contains(@id, 'apply')]")
        # click the link( i(key number) won't change even the DOM change)
        links[i].click()
        # switch driver to iframe
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id, 'grnhse_iframe')]"))
        job_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'app-title'))
        )
        job_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content"))
        )

        # converting from element to string
        job_description = job_description.text
        job_title = job_title.text

        # collect languages
        programming_language_lst = extract_programming_languages(job_description)

        # convert list to string
        programming_language = list_to_string(programming_language_lst)

        # retrieve url
        url = driver.current_url

        # print to terminal
        #print("")
        #print("----------" + job_title.text + " (Argo AI) ----------")
        #print(job_description.text)
        #print("")

        # input to csv file
        csv_writer.writerow(
            {'company': 'Argo-AI', 'job-title': job_title, 'url': url, 'programming-languages': programming_language, 'job-description': job_description})

        # get job description page DOM
        job = driver.current_url
        driver.get(job)
        back = driver.find_element_by_xpath("//div[contains(@class, 'button back')]")
        back.click()


with open('autonomous-vehicle-company-software-engineer.csv', 'w', newline='', encoding='UTF-8') as csv_file:
    fieldnames = ['company', 'job-title', 'url', 'programming-languages', 'job-description']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    get_waymo_software_engineer_job_information()
    get_tesla_engineer_job_information()
    get_gmcruise_engineer_job_information()
    get_argoai_engineer_job_information()
    driver.quit()



