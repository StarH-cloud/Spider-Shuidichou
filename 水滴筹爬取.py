import os
import json
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#根据浏览器安装相应的驱动
browser = webdriver.Edge()

# 打开网页
browser.get('https://www.shuidichou.com/cf/contribute/44abbd2d-8e57-420a-a152-6eeb6aa2d27b?channel=cf_homepage_dispose&sdreqid=bca6245d5eda4b6f8b69f2924e62f34d&skuId=155107796905713049&audience=&adCreativeId=adcre17171239016059877&adPositionId=posad15366707651239765&sdreqId=bca6245d5eda4b6f8b69f2924e62f34d&commonActId=10')
time.sleep(10)
start_time = time.time()    # 开始计时
# 要发送请求的 URL
url = 'https://api.shuidichou.com/api/cf/v5/detail/get'
# 请求头，根据实际情况设置
headers = {
    "User-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"
}
# 函数：进行POST请求
def get_data(page):
    # 请求体数据，例如一个字典
    data = {
        'size': '20',
        'infoUuid': '44abbd2d-8e57-420a-a152-6eeb6aa2d27b',
        'pageNum': page,
        # 'selfTag': 'zbCnHZ2EhCTy26Qcywy1728226866273',
        'degree': '1000',
    }
    # 发送 POST 请求
    response = requests.post(url, data=data, headers=headers)
    return response

# 函数：向下滑动，打开下一个POST请求
def open_five():
    for i in range(5):
        # 滑动到最下面
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        # 向上滚动到显示按钮的位置
        actions = ActionChains(browser)
        actions.scroll_by_amount(0, -500)  # 负数表示向上滚动，数值可根据需要调整
        actions.perform()
        time.sleep(1)
        # 鼠标移动到元素上进行点击
        element = browser.find_element(By.CLASS_NAME, 'open-more')  #点开一次增加4个
        actions = ActionChains(browser)
        actions.move_to_element(element).click().perform()
        time.sleep(1)
        try:
            element1 = browser.find_element(By.CLASS_NAME, 'close-text')
            actions1 = ActionChains(browser)
            actions1.move_to_element(element1).click().perform()
            time.sleep(1)
        except:
            pass

# 函数：获取表单数目，总共获得帮助的次数
def fortimes():
    # 要发送请求的 URL
    url = 'https://api.shuidichou.com/api/cf/v4/get-funding-info'

    # 请求头，根据实际情况设置
    headers = {
        "User-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"
    }
    # 请求体数据，例如一个字典
    data = {
        'infoUuid': '44abbd2d-8e57-420a-a152-6eeb6aa2d27b',
        'selfTag': 'zbCnHZ2EhCTy26Qcywy1728226866273',
        'skip': 'false',
        'userSourceId': '',
        'AuthorizationV2': 'G-7JLC-uRpWVFkVwgHi4NZa22oil_o5DyY1_ky9d6IA='
    }
    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=data)
    # 处理响应
    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)
        print(data['data']['baseInfo']['donationCount'])
        times = (int(data['data']['baseInfo']['donationCount'])//20)+2
        print(times)
        return times
    else:
        print(f"Request failed with status code: {response.status_code}")

# 设置存储路径
base_path = "D:\\Pycharm\\pythonProject1\\Test2"

for_time = fortimes()//30+1
print(for_time)
# for_time = 60
'''
# 开始爬取
for i in range(1,for_time):
    # 打开所有捐款页面，让页面加载完所有POST请求
    for i in range(1, for_time):
        # 点开5次，一次4个，会打开下一个请求
        open_five()
    html = get_data(50).text
    content = json.loads(html)
    print('-' * 50 + "第{}页".format(i) + '-' * 50)
    # 输出昵称
    a = 'nickname'  # 后期可以设置列表循环输出想要的
    for num in range(len(content['data']['list'])):
        print(content['data']['list'][num]['{}'.format(a)])
'''    
for a in range(0,for_time):
    for b in range(1,31):
        print(f'a={a},b={b}')
        # 调用函数进行POST请求
        html = get_data(int(a*30+b)).text
        content = json.loads(html)  # json.loads(): 对数据进行解码
        # 设置存储路径
        file_path = os.path.join(base_path, f"test{a}_{b}.json")
        # 打开文件，存入数据
        with open(file_path, 'a', encoding='utf-8') as f:  # 以写入模式打开文件
            json.dump(content, f, indent=4)  # 将 JSON 数据写入文件，并添加缩进以提高可读性
            # f.write('\n')
        c = a*30+b
        print('-' * 50 + f"{a}-{b}第{c}页"+ '-' * 50)
        # 输出昵称
        for num in range(len(content['data']['list'])):
            print(content['data']['list'][num]['nickname'])
        open_five()
    time.sleep(2)


end_time = time.time()
execution_time = end_time - start_time
print(f"程序运行了 {execution_time} 秒")


time.sleep(60000)
# browser.close()










