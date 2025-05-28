from bs4 import BeautifulSoup
import json
import requests
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
    # soup = BeautifulSoup(response.text, "lxml")
    data = json.loads(response.text)
    print(data['data']['baseInfo']['donationCount'])
    times = (int(data['data']['baseInfo']['donationCount']) // 20) + 1
    print(times)
else:
    print(f"Request failed with status code: {response.status_code}")
