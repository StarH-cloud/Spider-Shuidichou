'''
这是水滴筹爬取筹款案例和捐款记录的程序
'''
# TODO 1 筹款案例爬取
import json
import time
import requests
import pymongo
from pandas.core.interchange.dataframe_protocol import DataFrame

URL = ['https://api.shuidichou.com/api/charity/love-home/find-love-help-case-v2',
       'https://api.shuidichou.com/api/charity/love-home/find-rights-case']# 水滴筹的主页和更多
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
start_time = time.time()  # 开始计时

# todo 连接MongoDB，打开数据库，打开集合
client = pymongo.MongoClient('localhost', 27017)
db = client['Cases']      # 数据库文件
collection = db['cases']  # 数据库文档
# 授权码----报错data时，更换授权码，这也是一个问题！
AuthorizationV2 = 'TrYCxubWuKRI6CQfhgOiZ6d1iepKSUkwOoUY_nIoHDQ='

# todo 获取数据
for url in URL:
    # todo 参数设置
    HasNext = True  # 第一页存在
    page = 1

    while HasNext:
        data = {
            'currentPage': page,
            'pageSize': '10',
            'AuthorizationV2': AuthorizationV2
        }
        response = requests.post(url, data=data, headers=headers)
        content = json.loads(response.text)
        # todo 写入到数据库的集合中
        collection.insert_many(content['data']['caseInfoVoList'])
        # 输出显示
        print('-' * 25 + f"第{page}页" + '-' * 25)
        # todo 更新参数
        HasNext = content['data']['next']
        page += 1

end_time = time.time()
execution_time = end_time - start_time
print(f"程序运行了 {execution_time} 秒")
