from bs4 import BeautifulSoup
import requests

waymo_career = requests.get('https://waymo.com/joinus/').text

soup = BeautifulSoup(waymo_career, 'lxml')

# get the job title of software engineer
def get_waymo_software_engineer_job_information():
    software_engineer = soup.find('li', {'ng-if': "ctrl.categoryIsActive('Software Engineering', ['Mountain View, California, United States','New York, New York, United States','San Francisco, California, United States','Seattle, Washington, United States','Oxford, England, United Kingdom','Ann Arbor, Michigan, United States',])"})
    get_waymo_job_information(software_engineer)


def get_waymo_job_information(job_type):
    for job_link in job_type.find_all('a', {'class': 'ak-update-params'}, href=True):
        job_role_page = requests.get('https://waymo.com' + job_link['href']).text
        new_soup = BeautifulSoup(job_role_page, 'lxml')
        job_title = new_soup.find('div', {'class': 'career__title'}).text
        job_description = new_soup.find('div', {'class': 'career__description'}).text
        print("")
        print(job_title)
        print(job_description)
        print("")



get_waymo_software_engineer_job_information()


