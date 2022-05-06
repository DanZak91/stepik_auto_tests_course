from selenium import webdriver
import time, math, os

url = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(url)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button = browser.find_element_by_tag_name("button").click()

    #https://stepik.org/lesson/184253/step/5?unit=158843
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)

    x_element = browser.find_element_by_id('input_value').text
    x = calc(x_element)
    inques = browser.find_element_by_id('answer').send_keys(x)
    button2 = browser.find_element_by_tag_name("button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


