from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
print(driver.title)
driver.maximize_window()
driver.switch_to.frame(0)
dragg=driver.find_element_by_xpath("//div[@id='draggable']")
drop=driver.find_element_by_xpath("//div[@id='droppable']")
sleep(3)
action=ActionChains(driver)
action.drag_and_drop(dragg,drop).perform()
sleep(4)
driver.switch_to.default_content()

sleep(4)


driver.close()
driver.quit()

