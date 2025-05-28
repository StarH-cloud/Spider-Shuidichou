import json

import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"
}

def get_song(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    ranks = soup.select('.pc_temp_num')
    titles = soup.select('.pc_temp_songname')
    times = soup.select('.pc_temp_time')
    for rank, title, time in zip(ranks, titles, times):
        str1 = "".join(title.text.split())
        # print(str1)
        data = {
            'rank': rank.get_text().strip(),
            'song': str1.split("-")[0],
            'singer': str1.split("-")[1],
            'time': time.text.strip()
        }
        # 写入文件，注意⚠️文件名称是否要改
        # file = open('kugou500_1.txt', 'a', encoding='utf-8')
        # file.write(','.join([rank.get_text().strip(), str1.split("-")[0], str1.split("-")[1], time.text.strip()]))
        # file.write('\n')
        # file.close()

        with open('kugou500_2.txt', 'a', encoding='utf-8') as f:
            f.write(','.join([rank.get_text().strip(), str1.split("-")[0], str1.split("-")[1], time.text.strip()])+'\n')
        print(data)

if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i))for i in range(1,30)]
    for url in urls:
        get_song(url)
        # time.sleep(1)

