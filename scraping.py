import pandas as pd
import numpy as np
import re
import parameter
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

#webdriver microsoft edge
driver = webdriver.Edge('C:/Users/helmi/Downloads/edgedriver_win64 (2)/msedgedriver.exe')

#mengakses web linkedin
driver.get('https://www.linkedin.com')

# login
username = driver.find_element_by_name('session_key')
username.send_keys(parameter.email)
password = driver.find_element_by_name('session_password')
password.send_keys(parameter.password)
submit = driver.find_element_by_class_name('sign-in-form__submit-button')
submit.click()
sleep(10)

driver.get(parameter.siteQuery)
sleep(5)
wait = WebDriverWait(driver, 20)
links = driver.find_elements_by_xpath("//a[@class='disabled ember-view job-card-container__link']")
links =[link.get_attribute("href") for link in links]
sleep(1)

#webdriver microsoft edge
driver = webdriver.Edge('C:/Users/helmi/Downloads/edgedriver_win64/msedgedriver.exe')

#mengakses web linkedin
driver.get('https://www.linkedin.com')

# login
username = driver.find_element_by_name('session_key')
username.send_keys(parameter.email)
password = driver.find_element_by_name('session_password')
password.send_keys(parameter.password)
submit = driver.find_element_by_class_name('sign-in-form__submit-button')
submit.click()
sleep(2)

driver.get(parameter.siteQuery)
sleep(5)
wait = WebDriverWait(driver, 20)
links = driver.find_elements_by_xpath("//a[@class='disabled ember-view job-card-container__link']")
links =[link.get_attribute("href") for link in links]
sleep(1)

listTitle = []
listCompanies = []
listLocations=[]
listDescriptions=[]
for link in links :
    driver.get(link)
    sleep(5)
    sel= Selector(text=driver.page_source)
    titles = sel.xpath('//h1[@class="t-24 t-bold jobs-unified-top-card__job-title"]/text()').extract()
    listTitle.append(titles[0])
    companies = sel.xpath('//span[@class="jobs-unified-top-card__company-name"]').extract()
    listCompanies.append(companies[0])
    locations = sel.xpath('//span[@class="jobs-unified-top-card__bullet"]/text()').extract()
    listLocations.append(locations[0])
    descriptions = sel.xpath('//*[@id="job-details"]').extract()
    listDescriptions.append(descriptions[0])

#data cleaning
listCompanies2=[]
listLocations2=[]
listDescriptions2=[]
for company in listCompanies :
        company = BeautifulSoup(company,features='html.parser').text
        company = company.strip(' \n')
        listCompanies2.append(company)
for location in listLocations :
        location = BeautifulSoup(location,features='html.parser').text
        location = location.strip(' \n')
        listLocations2.append(location)
for description in listDescriptions :
        description = BeautifulSoup(description,features='html.parser').text
        description = re.sub(r'\n', '', description)
        listDescriptions2.append(description)

#exporting to csv
data = [listTitle,listCompanies2,listLocations2,listDescriptions2]        
data = np.transpose(data)
column = ['Title','Companies','Locations','Descriptions']
df = pd.DataFrame(data=data, columns=column)
df.to_csv('hasil.csv')


