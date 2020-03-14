from selenium import webdriver
import time
from time import sleep



driver=webdriver.Chrome(executable_path="E:\\Chromedriver.exe")


driver.get("https://www.amazon.in")

driver.maximize_window()

page_title=driver.title

print(page_title)
sleep(2)

Search_box=driver.find_element_by_xpath("(//input[@type='text'])[1]")
Search_box.send_keys("nokia")
sleep(3)
submit_bt=driver.find_element_by_xpath("(//input[@type='submit'])[1]")
submit_bt.click()
sleep(3)
actual_product_list=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
len(actual_product_list)
print(len(actual_product_list))

sleep(3)
expected_product_list=[ 'Nokia 4.2 (Black, 3GB RAM, 32GB Storage)',
                         'Nokia 105 2019 (Single SIM, Black)',
                         'Nokia 3310 (Dark Blue)',
                        'Nokia 6.1 Plus (Black, 6GB RAM, 64GB Storage)'
                         'Nokia 2.2 2/16 Black']
for expected_product in expected_product_list:
    for product in actual_product_list:
        #print("product_list: ",product.text)
         if product.text==expected_product:
                product.click()
                sleep(4)

                p_window=driver.current_window_handle
                window_list=driver.window_handles
                for window in window_list:
                    if (window!=p_window):
                        driver.switch_to.window(window)
                        product_title=driver.find_element_by_id("productTitle")
                        product_title=product_title.text
                        print( product_title)
                        sleep(4)

                        product_prise_block=driver.find_element_by_id("priceblock_ourprice")
                        product_prise_block=product_prise_block.text
                        print( product_prise_block)
                        sleep(4)

                        product_rating=driver.find_element_by_id("acrCustomerReviewText")
                        product_rating=product_rating.text
                        print(product_rating)
                        sleep(10)

                        driver.close()
                        sleep(4)

                        driver.switch_to.window(p_window)
                        sleep(4)











sleep(4)

driver.close()
driver.quit()