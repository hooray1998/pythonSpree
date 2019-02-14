# -*- coding:utf-8 -*-
 
import sys

#===============================================================
#    TITLE:  sys
#===============================================================


sys.argv
sys.exc_info() # 输出异常信息
# example
try:
    x = 1/0
except Exception as msg:
    print(msg)
    print(sys.exc_info())
print(sys.path) # 搜索模块的路径和查找顺序
print(sys.platform)
print(sys.version)
print(sys.version_info)
# sys.exit(0) # 正常退出

print("#===============================================================")
print("#    TITLE:  datetime")
print("#===============================================================")

import datetime as dt
d1 = dt.date(2007,9,9) # date(year, month, day) 
d2 = dt.date(2008,9,9)
print(d1)
print(d1.strftime('%A, %m/%d/%y'))
print(d1.strftime('%a, %m-%d-%Y'))

d = d2 - d1
print(type(d)) # timedelta(day, hr, min, sec, us)
print(d)
print(d.days)
print(d.seconds)

print(dt.date.today())

t1 = dt.time(15, 38) # time(hour, min, sec, us)
t2 = dt.time(18)

print(t1)
print(t1.strftime('%I:%M, %p'))
print(t1.strftime('%H:%M:%S, %p'))

d1 = dt.datetime.now() # datetime(year, month, day, hr, min, sec, us)
print(d1)
d2 = d1 + dt.timedelta(30)
print(d2)
print(dt.datetime.strptime('2/10/01', '%m/%d/%y'))




print("#===============================================================")
print("#    TITLE:  collections 模块：更多数据结构")
print("#===============================================================")


import collections
# 3.1 计数器
# 可以使用 Counter(seq) 对序列中出现的元素个数进行统计。

# 例如，我们可以统计一段文本中出现的单词及其出现的次数：
from string import punctuation  #所有标点
sentence = "One, two, three, one, two, tree, I come from China."
words_count = collections.Counter(sentence.translate(punctuation).lower().split())
print(words_count)

# 3.2 双端队列
# 双端队列支持从队头队尾出入队：

dq = collections.deque()
for i in range(10):
    dq.append(i)
print(dq)
for i in range(10):
    print(dq.pop(), end='')
print()
for i in range(10):
    dq.appendleft(i)
print(dq)
for i in range(10):
    print(dq.popleft(),end = '')
#   与列表相比，双端队列在队头的操作更快：


# 3.3 有序字典
# 字典的 key 按顺序排列：

items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)
regular_dict = dict(items)
ordered_dict = collections.OrderedDict(items)
print('Regular Dict:')
for k, v in regular_dict.items():
    print(k, v)
print('Ordered Dict:')
for k, v in ordered_dict.items():
    print(k, v)

# 3.4 带默认值的字典
# 对于 Python 自带的词典 d，当 key 不存在的时候，调用 d[key] 会报错，但是 defaultdict 可以为这样的 key 提供一个指定的默认值，我们只需要在定义时提供默认值的类型即可，如果 key 不存在返回指定类型的默认值：


dd = collections.defaultdict(list)
print(dd["foo"])
dd = collections.defaultdict(int)
print(dd["foo"])
dd = collections.defaultdict(float)
print(dd["foo"])


#===============================================================
#    TITLE:  迭代器
#===============================================================

print("# 另一种迭代键的方式")
d={'name':'appleyk','age':26,'gender':'F','job':'coder'} 
print("迭代key") 
for s in d: #迭代key 
    print(s) 
print("# set 是可迭代的")
from collections import Iterable
S = {"name","age","sex","adress"}  
print('判断set是否属于可迭代的对象    :' ,isinstance(S,Iterable))

print("# 同时迭代元素和下标")
for index,key in enumerate({'first':1,'second':2,'third':3}):  
    print(index,":",key)  
for index,key in enumerate({'first','second','third'}):  
    print(index,":",key)  


print("# 同时迭代列表元素中的每个元素的值")
for x in [(1,2,3),(4,5,6,),(7,8,9)]:
    print(x)
for x,y,z in [(1,2,3),(4,5,6,),(7,8,9)]:
    print(x,y)
for x,_,_ in [(1,2,3),(4,5,6,),(7,8,9)]:
    print(x)

# 通过next迭代
L = ['appleyk','F',26,'Python3']  
it = iter(L) #获得list的迭代器对象  
while True:  
    try:
        x=next(it)#然后我们用next对这个对象进行遍历  
        # x=it.__next__()
        print(x)  
        #next会不会溢出呢？它会一直访问停不下来吗？  
    except StopIteration:
        break

# 下面两行效果相同
it2 = L.__iter__()
it3 = iter(L) # 两者都是返回一个迭代器对象,同一个迭代器可以返回多个迭代器对象,互不干扰

# 下面两行效果相同 (那是不是说所有next()可操作的对象中都必须实现__next__()方法), 其他函数应该也同理
next(it2) # 通过next迭代
it3.__next__()

# 反转函数,也是返回一个迭代器对象
r = reversed(L)

# 实现一个简单的迭代器
class MyIterator(object):  
    def __init__(self,step):  
        self.step=step  
      
    def __next__(self):  
        if self.step==0:  
            raise StopIteration  
        self.step-=1  
        return self.step  
      
    def __iter__(self):  
        return self  


#===============================================================
#    TITLE:  迭代器后续内容暂未学习
#===============================================================


#===============================================================
#    describe:  re(正则匹配模块,暂未学习)
#===============================================================


#===============================================================
#    describe:  request
#===============================================================
import requests


#浏览器伪装-字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("https://www.zhihu.com/explore", headers=headers)
print(response.text)


#===============================================================

import urllib.request   # request
import json
import os

#响应
response = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json")

#列表－字典数据
hero_json = json.loads(response.read())  #接受相应，读取内容
hero_num = len(hero_json)

# print(hero_json)
print("hero_num : " , str(hero_num))

#英雄有几个皮肤
#herolist.json文件中有“skin_name”字段，我们只要解析这个字段就可以获取皮肤数量和皮肤名称

printNum = 0
for  item in hero_json:
    hero_name = item['cname']
    skin_names = item['skin_name'].split('|')  #结果为列表
    skin_num = len(skin_names)
    print('hero_name: ', hero_name)
    print('skin_names :', skin_names)
    print('skin_num: ' + str(skin_num))
    printNum += 1
    if printNum>5:
        break

#===============================================================
#    describe:  debug
#===============================================================
# Methon 1:  print()
# Methon 2:  assert()
# Methon 3:  logging
import logging  
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='test.log',  # 输出到文件
                    filemode='w')  
  
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')  

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


# Methon 4: pdb
# -*- coding:utf-8 -*-
import pdb
 
def f(s):
    n=int(s)
    pdb.set_trace() # 运行到这里会自动暂停
    result = 10/n
    return result
s = '0'
n = int(s)
print("tset1")
k=2**3
pdb.set_trace() # 运行到这里会自动暂停
f(input())

