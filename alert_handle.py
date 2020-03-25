from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert



driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
sleep(3)
driver.maximize_window()
sleep(3)

alert=Alert(driver)

click_button=driver.find_element_by_xpath("(//button[text()='Click me!'])[1]")
click_button.click()
sleep(3)
#alert=Alert(driver)

driver.switch_to.alert
alert_text=alert.text
print(alert.text)
alert.accept()

sleep(3)

click_button=driver.find_element_by_xpath("(//button[text()='Click me!'])[2]")
click_button.click()
sleep(3)
driver.switch_to.alert
alert_text=alert.text
print(alert.text)
alert.accept()
sleep(4)

click_prompt_box=driver.find_element_by_xpath("//button[text()='Click for Prompt Box']")
click_prompt_box.click()

sleep(3)

driver.switch_to.alert
alert.send_keys("AmolHarale")
sleep(2)

alert_text=alert.text
print(alert.text)
alert.accept()

#alert.dismiss()
sleep(3)








driver.close()
driver.quit()
