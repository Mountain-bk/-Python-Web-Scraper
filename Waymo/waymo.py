from bs4 import BeautifulSoup
import requests

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
    print("---Waymo Software Job Information---")
    for job_link in job_type.find_all('a', {'class': 'ak-update-params'}, href=True):
        # get the specific job link page
        job_role_page = requests.get('https://waymo.com' + job_link['href']).text

        new_soup = BeautifulSoup(job_role_page, 'lxml')
        job_title = new_soup.find('div', {'class': 'career__title'}).text
        job_description = new_soup.find('div', {'class': 'career__description'}).text
        print("")
        print("----------" + job_title.text + " (Waymo) ----------")
        print(job_description)
        print("")

get_waymo_software_engineer_job_information()
get_waymo_system_engineer_job_information()
