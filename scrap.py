from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
from bs4 import BeautifulSoup
import requests

#constants
URL = "https://www.tnebnet.org/atm/tariffMaster"

driver = webdriver.Firefox()

driver.get(URL)
source = driver.page_source
unit_consume = driver.find_element_by_xpath('//*[@id="calculator:unit"]')
element = driver.find_element_by_xpath('//*[@id="calculator:tarifftype"]')
calc_button = driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[4]/td/fieldset/div/table[2]/tbody/tr/td[2]/button/span')
action = ActionChains(driver)
select_object = Select(element)
select_object.select_by_value("DOMESTIC")
action.send_keys_to_element(unit_consume,500)
action.click(on_element=calc_button)
action.perform()

# response = requests.get(URL)
# print(response.text)
soup = BeautifulSoup(source,'lxml')
print(soup)
