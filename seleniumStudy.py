# 初始化
from selenium import webdriver
import selenium
import time
browser = webdriver.Edge()
browser.get('https://www.taobao.com')
# print(browser.page_source)
# time.sleep(2)
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_i = browser.find_element('id', 'q')
# print(input_first.text, input_second.text, input_third.text,input_i)
print(input_i)

browser.close()