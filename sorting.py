from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://jqueryui.com")
print(driver.title)
driver.maximize_window()
#driver.switch_to.frame(0)
sleep(3)
selectable=[]
selectable=driver.find_element_by_xpath("//div[@id='sidebar']/aside[1]/ul/li[4]/a")
selectable.click()

#print(selectable.text)
sleep(3)
sortable=driver.find_element_by_xpath("//div[@id='sidebar']/aside[1]/ul/li[5]/a")
sortable.click()
#len(sortable)
#print(len(sortable))
#for sort in sortable:
#dec=driver.find_elements_by_id("//ul[@id='sortable']")

item=driver.find_elements_by_xpath("//li[@class='ui-state-default ui-sortable-handle']")
for itm in item:

    print(": ")

#item.reverse()
#print(item)








sleep(3)

#sorting=driver.find_element_by_xpath("//a[text()='']")

driver.close()
driver.quit()