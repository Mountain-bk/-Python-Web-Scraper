from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.delete_all_cookies()


def get_tesla_engineer_job_information():
    print("---Tesla Software Job Information---")
    # fill in keyword you want to search
    keyword = 'software'
    driver.get('https://www.tesla.com/jp/careers/search#/?keyword=' + keyword + '&department=4&country=0')
    # 2 seconds to complete the load
    time.sleep(2)
    tesla_soup = BeautifulSoup(driver.page_source, 'lxml')
    job_list = tesla_soup.find('tbody', attrs={'data-reactid': ".0.0.1.0.0.1"})
    with open('tesla-software-engineer.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        fieldnames = ['job-title', 'job-description']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for job_title in job_list.find_all('th', {'class': 'listing-title'}):
            try:
                link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '" + job_title.text + "')]"))
                )
                link.click()
                # job title
                title = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), '" + job_title.text + "')]"))
                )
                # job description
                job_description = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@class = 'notranslate']"))
                )

                # print to terminal
                print("")
                print("----------" + title.text + " (Tesla) ----------")
                print(job_description.text)
                print("")

                # input to csv file
                csv_writer.writerow({'job-title': title.text, 'job-description': job_description.text})
            finally:
                driver.back()
    driver.quit()





get_tesla_engineer_job_information()
