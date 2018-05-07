# coding=utf-8
# Created by DockerChen
import json,os

# 伪装成正规的浏览器来访问网站，防止被拦截
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Moziversiona/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

f = open('data.json', 'r', encoding='UTF-8')
data = f.read()
f.close()
# print(data)

data2 = json.loads(data)
# print(data2)

num = 0  # 统计卡牌数量

version = []
for i in data2:
    try:
        if i['set']:
            version.append(i['set'])
            num = num + 1
            # print(num)
    except:
        pass

version = set(version)
# print(version)
# print(len(version))

for v in version:
    path = 'templates/' + v + '.html'

    # 判断文件是否存在，避免重新创建
    if os.path.exists(path) == False:
        f = open(path, 'w')
        f.close()
