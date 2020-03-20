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
action.move_to_element(tenders).perform()

sleep(4)

Aiims_tenders=driver.find_element_by_xpath("(//span[@class='menu-title'])[41]")
action.move_to_element(Aiims_tenders).click().perform()



sleep(2)
tenders_title_list=[]

tenders_title=driver.find_elements_by_xpath("//tbody/tr/td/a")
sleep(2)
for tenders in tenders_title:
    print(tenders.text)






sleep(3)



driver.close()
driver.quit()