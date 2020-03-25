from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep


driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://jqueryui.com")
print(driver.title)
driver.maximize_window()
#driver.switch_to.frame(0)
sleep(3)
RE_siza=driver.find_element_by_xpath("//div[@id='sidebar']/aside[1]/ul/li[3]/a")
RE_siza.click()
sleep(3)
Resize_Webelement=driver.find_element_by_id("resizable")
#Resize_Webelement.click()
action=ActionChains(driver)
action.dragAndDropBy(Resize_Webelement, 150, 100).perform()




sleep(3)

driver.close()
driver.quit()