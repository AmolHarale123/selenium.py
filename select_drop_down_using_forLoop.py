from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://www.facebook.com")
sleep(4)
print(driver.title)
driver.maximize_window()
sleep(4)



#selsct_custom=driver.find_element_by_xpath("//div/span/span[3]")
#selsct_custom.click() -----------using full Xpath
sleep(4)

#select_your_pronoun=driver.find_element_by_xpath('//select[@aria-label="Select your pronoun"]')
selsct_custom=driver.find_element_by_xpath("(//span[@class='_5k_2 _5dba'])")
action=ActionChains(driver)
i=1
for select in selsct_custom:
    select_class=Select(selsct_custom)
    select_class.deselect_by_value(i)
    i=i+1
    print(select_class)



#select_class=select_class.text
#select_class.select_by_index(1)


sleep(3)

driver.close()
driver.quit()
