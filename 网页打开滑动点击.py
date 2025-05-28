from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Edge()
browser.get('https://www.shuidichou.com/cf/contribute/44abbd2d-8e57-420a-a152-6eeb6aa2d27b?channel=cf_homepage_dispose&sdreqid=bca6245d5eda4b6f8b69f2924e62f34d&skuId=155107796905713049&audience=&adCreativeId=adcre17171239016059877&adPositionId=posad15366707651239765&sdreqId=bca6245d5eda4b6f8b69f2924e62f34d&commonActId=10')
time.sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 执行滚动脚本，没问题
# wait = WebDriverWait(browser, 10)
# div_element = wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'charge-btn-icon')))
# button = div_element.find_element(By.TAG_NAME, 'button')
# button = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@class="open-more-wrapper"]/button')))
# button = browser.find_element(By.CLASS_NAME, 'charge-btn-icon')
# button.click()
for i in range(5):
    # 滑动到最下面
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # 向上滚动到显示按钮的位置
    actions = ActionChains(browser)
    actions.scroll_by_amount(0, -500)  # 负数表示向上滚动，数值可根据需要调整
    actions.perform()
    time.sleep(2)
    # 鼠标移动到元素上进行点击,点开一次增加4个
    element = browser.find_element(By.CLASS_NAME, 'open-more')
    actions = ActionChains(browser)
    actions.move_to_element(element).click().perform()
    time.sleep(2)



time.sleep(10)
# browser.close()