from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import  By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

from time import sleep



driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")

driver.get("https://www.google.com/")
driver.maximize_window()
page_title=driver.title
print(page_title)
search_box=driver.find_element_by_xpath('//input[@type="text"]')

driver.implicitly_wait(5)
action=ActionChains(driver)
#action.key_down(Keys.SHIFT,search_box).send_keys("amol").key_up(Keys.SHIFT,search_box).perform()
search_box.click()
driver.implicitly_wait(5)
action.key_down(Keys.SHIFT).send_keys("hplaptop").key_up(Keys.SHIFT).perform()
driver.implicitly_wait(3)
action.send_keys(Keys.ENTER).perform()
sleep(4)



driver.close()
driver.quit()