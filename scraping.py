import parameter
from parsel import Selector
from time import sleep
from selenium.webdriver.edge.service import Service
from selenium import webdriver
import getpass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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

for link in links :
    driver.get(links[0])
    sleep(5)
    # moreinfo =driver.find_element_by_class_name('artdeco-card__action')
    # moreinfo.click()
    sel= Selector(text=driver.page_source)

    title = sel.xpath('/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div[2]/h1')
    content = sel.xpath('//*[@id="job-details"]/span/text()')




