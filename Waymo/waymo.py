from bs4 import BeautifulSoup
import requests
import csv

waymo_career = requests.get('https://waymo.com/joinus/').text
waymo_soup = BeautifulSoup(waymo_career, 'lxml')

def get_waymo_software_engineer_job_information():
    print("---Waymo Software Job Information---")
    software_engineer = waymo_soup.find('li', {'ng-if': "ctrl.categoryIsActive('Software Engineering', ['Mountain View, California, United States','New York, New York, United States','San Francisco, California, United States','Seattle, Washington, United States','Oxford, England, United Kingdom','Ann Arbor, Michigan, United States',])"})
    with open('waymo-software-engineer.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        fieldnames = ['job-title', 'job-description']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for job_link in software_engineer.find_all('a', {'class': 'ak-update-params'}, href=True):
            # get the specific job link page
            job_role_page = requests.get('https://waymo.com' + job_link['href']).text
            new_soup = BeautifulSoup(job_role_page, 'lxml')
            job_title = new_soup.find('div', {'class': 'career__title'}).text
            job_description = new_soup.find('div', {'class': 'career__description'}).text

            # print to terminal
            print("")
            print("----------" + job_title + " (Waymo) ----------")
            print(job_description)
            print("")

            # input to csv file
            csv_writer.writerow({'job-title': job_title, 'job-description': job_description})

get_waymo_software_engineer_job_information()
