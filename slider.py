from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
print(driver.title)
driver.maximize_window()
driver.switch_to.frame(0)
dragg=driver.find_element_by_xpath("//div[@id='draggable']")
drop=driver.find_element_by_xpath("//div[@id='droppable']")
sleep(3)
action=ActionChains(driver)
action.drag_and_drop(dragg,drop).perform()
sleep(4)
driver.switch_to.default_content()
sleep(4)

slider_link=driver.find_element_by_xpath("//a[text()='Slider']")
driver.execute_script("arguments[0].scrollIntoView();", slider_link)
slider_link.click()
sleep(4)
driver.execute_script("window.scrollBy(0,-100);")
sleep(2)

iframe=driver.find_elements_by_tag_name("iframe")[0]
driver.switch_to.frame(iframe)
sleep(3)


#sliding_obj=driver.find_element_by_id("slider")
slide_obj=driver.find_element_by_css_selector("#slider > span")
action=ActionChains(driver)
sleep(3)
action.drag_and_drop_by_offset(slide_obj,100,0).perform()
sleep(4)

driver.close()
driver.quit()
