from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
def test_zalupa():

    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value").text
    y=calc(x_element)
    otvet = browser.find_element(By.ID, "answer")
    otvet.send_keys(y)
    button=browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox=browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio=browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio.click()
    button.click()
    time.sleep(10)



