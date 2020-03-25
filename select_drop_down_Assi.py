from selenium import webdriver
from selenium.webdriver.support.select import Select

from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://www.facebook.com")
sleep(4)
print(driver.title)
driver.maximize_window()
sleep(4)


selsct_custom=driver.find_element_by_xpath("//div[2]/div/div[2]/div/div/div/div[1]/form/div[1]/div[6]/span/span[3]/label").click()
sleep(4)

select_your_pronoun=driver.find_element_by_xpath('//select[@aria-label="Select your pronoun"]')
select_class=Select(select_your_pronoun)
sleep(5)
#select_class=select_class.text
select_class.select_by_index(0)

sleep(3)
select_class.select_by_value("1")


sleep(3)

select_class.select_by_value("2")
sleep(4)
#select_class.select_by_value("3")
sleep(4)
driver.close()
driver.quit()