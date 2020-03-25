from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://jqueryui.com/accordion/")
print(driver.title)
driver.maximize_window()
driver.switch_to.frame(0)
sleep(4)

content_head=driver.find_elements_by_css_selector('#accordion > h3')
print("length of content_Head:", len(content_head))
sleep(3)
action=ActionChains(driver)

i=1
for content in content_head:

    action.move_to_element(content).click().perform()
    driver.execute_script("arguments[0].scrollIntoView();",content)
    sleep(7)
    Head_content=driver.find_element_by_css_selector('div[aria-labelledby="ui-id-' +str(i)+ '"] > p')
    Head_content=Head_content.text
    sleep(3)

    print("content of section: ", Head_content)
    print("-----------------------------------")

    i+=+2
    sleep(4)











driver.close()
driver.quit()