from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")

driver.get("https://aiims.edu/en.html")
driver.maximize_window()

page_title=driver.title
sleep(4)

print(page_title)
tenders=driver.find_element_by_xpath("(//span[@class='menu-title'])[40]")
sleep(2)

action=ActionChains(driver)
action.move_to_element(tenders).perform()
Award_letter=driver.find_element_by_xpath("(//span[@class='menu-title'])[42]")

action.move_to_element(Award_letter).click().perform()
#Award_letter.click()
sleep(4)

driver.close()
driver.quit()


