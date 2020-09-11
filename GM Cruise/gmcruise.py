
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.delete_all_cookies()



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
    with open('gmcruise-software-engineer.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        fieldnames = ['job-title', 'job-description']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for link in driver.find_elements_by_xpath("//a[contains(@class, 'JobTable--job--i8IkL')]"):
            default_handle = driver.current_window_handle
            link.click()
            window = driver.window_handles
            driver.switch_to.window(window[1])
            title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "app-title"))
            )
            job_description = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "content"))
            )

            # print to terminal
            print("")
            print("----------" + title.text + " (GM Cruise) ----------")
            print(job_description.text)
            print("")

            # input to csv file
            csv_writer.writerow({'job-title': title.text, 'job-description': job_description.text})

            driver.close()
            driver.switch_to.window(default_handle)
    driver.quit()


get_gmcruise_engineer_job_information()
