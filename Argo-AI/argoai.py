
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.delete_all_cookies()

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
    with open('argoai-software-engineer.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        fieldnames = ['job-title', 'job-description']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
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

            # print to terminal
            print("")
            print("----------" + job_title.text + " (Argo AI) ----------")
            print(job_description.text)
            print("")

            # input to csv file
            csv_writer.writerow({'job-title': job_title.text, 'job-description': job_description.text})

            # get job description page DOM
            job = driver.current_url
            driver.get(job)
            back = driver.find_element_by_xpath("//div[contains(@class, 'button back')]")
            back.click()
    driver.quit()



get_argoai_engineer_job_information()
