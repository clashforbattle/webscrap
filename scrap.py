from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
#constants
driver.get("https://www.tnebnet.org/atm/tariffMaster")
unit_consume = driver.find_element_by_xpath('//*[@id="calculator:unit"]')
element = driver.find_element_by_xpath('//*[@id="calculator:tarifftype"]')
calc_button = driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[4]/td/fieldset/div/table[2]/tbody/tr/td[2]/button/span')
action = ActionChains(driver)
#actions
def scrap_unit_price():
    pass
def feed(consume):
    select_object = Select(element)
    select_object.select_by_value("DOMESTIC")
    action.send_keys_to_element(unit_consume,consume)
    action.click(on_element=calc_button)
    action.perform()
    
    return consume,price_for_consume
for i in range(0,5050,50):
    with open("data.txt",'r+') as data:
        data.append(feed(i))