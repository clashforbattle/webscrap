from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from time import sleep
import csv,random


driver = webdriver.Firefox()
def feed(consume):
    driver.get("https://www.tnebnet.org/atm/tariffMaster")
    unit_consume = driver.find_element_by_xpath('//*[@id="calculator:unit"]')
    element = driver.find_element_by_xpath('//*[@id="calculator:tarifftype"]')
    calc_button = driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[4]/td/fieldset/div/table[2]/tbody/tr/td[2]/button/span')
    action_in = ActionChains(driver)
    select_object = Select(element)
    select_object.select_by_value("DOMESTIC")
    action_in.send_keys_to_element(unit_consume,consume)
    action_in.click(on_element=calc_button)
    action_in.perform()
    sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    a = soup.find_all("span")
    return a[-4].text

data = []

for i in range(0,2000,100):
    data.append([i,feed(i)])

with open("data.txt",'r+') as data1:
        csvwriter = csv.writer(data1)
        for i in data:
            csvwriter.writerow(i)