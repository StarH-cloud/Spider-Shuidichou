'''
response = requests.get(URL,headers=headers)
soup = BeautifulSoup(response.text, "lxml")
print(response.status_code) # 状态码
print(soup.prettify())    # prettify()方法把要解析的字符串以标准的缩进格式输出
ranks = soup.select('.woo-like-count')
print(ranks)
print(soup.find_all(attrs={'class':'woo-like-count'}))
'''
'对于JSON文件的处理'
# print(type(trans_dict))
# print(trans_dict['data']['list'])
# print(trans_dict['data']['list'][10])
# print(len(trans_dict['data']['list']))
# print(trans_dict['trans_result']['data'][0]['src'])