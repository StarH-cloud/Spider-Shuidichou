import requests
from bs4 import BeautifulSoup

headers = {
    "User-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 Edg/127.0.0.0"
}

# response = requests.get("https://www.kugou.com/yy/rank/home/2-8888.html", headers=headers)
# html = response.text
# print(response.status_code) # 状态码
# print(response.text)  # 整个HTML文本
# soup = BeautifulSoup(html, "lxml")  # lxml HTML解析器，速度快，容错能力强，推荐使用
# print(soup.prettify())    # prettify()方法把要解析的字符串以标准的缩进格式输出
'''  <title>
   酷狗TOP500_排行榜_乐库频道_酷狗网
  </title>'''
# print(soup.head.title)  #输出： <title>酷狗TOP500_排行榜_乐库频道_酷狗网</title>
# print(type(soup.head.title))  #输出： <class 'bs4.element.Tag'>
# print(soup.head.title.string)   #输出： 酷狗TOP500_排行榜_乐库频道_酷狗网
# print(soup.head.title.text)   #输出： 酷狗TOP500_排行榜_乐库频道_酷狗网
# d = soup.find_all(attrs={'class':'pc_temp_songname'})
# print(d)
# print(type(d))  # <class 'bs4.element.ResultSet'>
'''# 这是一个<class 'bs4.element.ResultSet'>类型的列表，列表，
# 列表中每个都是<class 'bs4.element.Tag'>
<a class="pc_temp_songname" data-active="playDwn" data-index="21" hidefocus="true" href="https://www.kugou.com/mixsong/ac5xvf43.html" title="陈墨一（吖毛） - 你答应我的事 (件件没着落)">
									你答应我的事 (件件没着落)
																		<span style="color: #999;"> - 陈墨一（吖毛）</span>
</a>
'''
# print(list(d)[0].text)
# print(len(list(d)[0].text))
# print(list(d)[0].text.strip())  # 去掉左右的空格
# print(type(list(d)[0].text))
# print(type(list(d)[0]))
# for i in soup.find_all(attrs={'class':'pc_temp_songname'}):
#     # print(i.text)
#     # print(type(i.text))
#     # print(i.span.string)    # 只能得到span中的内容
#     # a = i.text.split()  # 讲字符串按空格分开，形成列表
#     # print(type(a))
#     # b = ' -连接符- '.join(a)
#     # print(b)
#     print(''.join(i.text.split()))  # 使用空连接起来，相当于去掉所有空格

# top = soup.select('.pc_temp_songname')

# for i in top:
#     a = "".join(i.text.split())
#     print(a)

# 下面是一个可以实现的部分
for i in range(30):
    response = requests.get("https://www.kugou.com/yy/rank/home/{}-8888.html".format(i), headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    ranks = soup.select('.pc_temp_num')
    top = soup.select('.pc_temp_songname')
    for rank, song in zip(ranks,top):
        r = rank.text.strip()
        s = "".join(song.text.split()).split("-")
        print(r+"歌曲："+s[0]+"  歌手："+s[1])



