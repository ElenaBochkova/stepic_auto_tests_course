from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    book = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book.click()
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    element = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.send_keys(y)
    element = browser.find_element_by_id("solve")
   # browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()