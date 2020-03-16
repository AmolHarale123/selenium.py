from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import  By
from selenium.webdriver.remote.webelement import WebElement



driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://aiims.edu/en.html")

sleep(4)
driver.maximize_window()
page_title=driver.title

sleep(4)

tenders=driver.find_element_by_xpath("(//span[@class='menu-title'])[40]")
sleep(2)
action=ActionChains(driver)
action.move_to_element(tenders).double_click().perform()

sleep(4)
tenders_title_list=[]

tenders_title=driver.find_element_by_xpath("(//div[@style='float: left; width: 100%;'])")
#action=ActionChains(tenders_title)
action.move_to_element(tenders_title)

#action.context_click("Tender Title").perform()

#action.move_to_element(tenders_title).perform()
sleep(3)



driver.close()
driver.quit()