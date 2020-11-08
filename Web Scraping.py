import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.error
# import urllib.request, urllib.error, urllib.parse
import json     #导入json
# - Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# - Actual data: http://py4e-data.dr-chuck.net/comments_275916.json (Sum ends with 15)



url = 'http://py4e-data.dr-chuck.net/comments_761276.xml'   # 指定URL
uh = urllib.request.urlopen(url)
data = uh.read()    # 获取网页数据

print('Retrived', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')   #查找count标签
# counts = tree.findall('comments/comment/count')
# 查找count可以使用上面这行语句

print('Count:', len(counts))

res = 0
for count in counts:
    res = res + int(count.text)
print('Sum:', res)


url = input('Enter url: ')
print('Retriving', url)
uh = urllib.request.urlopen(url).read()
print('Retrived', len(uh), 'characters')
js = json.loads(uh)
# 观察文档结构，js为字典，js['comments']为由字典组成的list
res = 0
for comment in js['comments']:
    res = res + comment['count']
print('Sum:', res)


target = 'http://py4e-data.dr-chuck.net/json?'  # 使用这个接口，需要 key参数且值为42
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})
# 对字符串进行url编码，直接传递参数和值构成的字典
print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
# print(json.dumps(js, indent = 4)) #查看接收到的文件结构
print('Place id', js['results'][0]['place_id'])


target = 'http://py4e-data.dr-chuck.net/json?'
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key': 42})


print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
# print(json.dumps(js, indent = 4)) 
print('Place id', js['results'][0]['place_id'])



