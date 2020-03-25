from selenium import webdriver

from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://jqueryui.com/accordion/")
print(driver.title)
driver.maximize_window()
driver.switch_to.frame(0)
sleep(4)
#  dot(.) represents class in css selector
#section_two_head = driver.find_ele0ment_by_css_selector("div[class='ui-id-3']")
# section_two_head = driver.find_element_by_css_selector(".ui-id-3")
print("----section.......1----")
content_head_1=driver.find_element_by_css_selector('div[aria-labelledby="ui-id-1"]>p')
print(content_head_1.text)

sleep(4)
print("----section.......2----")
section_head_2=driver.find_element_by_css_selector("#ui-id-3")
section_head_2.click()
# element got loaded within 2 secs still the sleep will apply for 5 secs
sleep(2)
#  hash(#) represents class in css selector
content_head_2=driver.find_element_by_css_selector("#ui-id-4 > p")
print(content_head_2.text)

sleep(2)
print("----section.......3----")
section_head_3=driver.find_element_by_css_selector("#ui-id-5")
section_head_3.click()
sleep(2)
content_head_3=driver.find_element_by_css_selector("#ui-id-6 > p")
print(content_head_3.text)
sleep(2)
print("----section.......4.0----")
section_head_4=driver.find_element_by_css_selector("#ui-id-7")
section_head_4.click()
sleep(2)
content_head_4_0=driver.find_element_by_css_selector("#ui-id-8 > p:nth-child(1)")
print(content_head_4_0.text)
sleep(2)
print("----section.......4.1----")
content_head_4_1=driver.find_element_by_css_selector("#ui-id-8 > p:nth-child(2)")
print(content_head_4_1.text)



driver.close()
driver.quit()
