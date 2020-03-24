from selenium import webdriver
from selenium.webdriver.support.select import Select

from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://www.facebook.com")
sleep(4)
print(driver.title)
driver.maximize_window()
#driver.switch_to.frame(0)
sleep(4)
select_birtday_month=driver.find_element_by_xpath("//select[@id='month']")
#select_birtday_month.click()
select_class=Select(select_birtday_month)
select_class.select_by_index(0)

sleep(4)

select_class.select_by_value("4")
sleep(2)
select_class.select_by_visible_text("Feb")
sleep(4)

driver.close()
driver.quit()