from selenium import webdriver

from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://jqueryui.com/accordion/")
print(driver.title)
driver.maximize_window()
driver.switch_to.frame(0)
sleep(4)





driver.close()
driver.quit()