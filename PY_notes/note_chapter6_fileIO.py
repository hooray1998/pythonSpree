# -*- coding:utf-8 -*-
 

#===============================================================
#    describe:  6.1
#===============================================================

print("f.readlines() 返回一个列表")
# 模式: 'w', 'r', 'a', 'w+'
# seek 的使用, seek之后读的是之后的内容

# NOTE: python3默认是unicode编码
# text.encode('utf-8')
# data.decode('utf-8')
#example
# GBK转化为Utf-8过程:
# 1, encode('unicode'); 2, decode('utf-8');

text = '朱亚非'
print(type(text),len(text),text)
b = text.encode('utf-8')
print(type(b),len(b),b)
u = b.decode('utf-8')
print(type(u),len(u),u)

# NOTE  若为模式r,上次w入未关闭之前打开读取并不更新

f = open('newfile.txt','w')
f.write('hello world')
# f.close()
g = open('newfile.txt', 'r')
print(repr(g.read()))

# NOTE 使用with打开后自动close,推荐



#===============================================================
print("# TITLE: 1.2 StringIO和BytesIO")
# 很多时候，数据读写不一定是文件，也可以在内存中读写。

from io import StringIO
f = StringIO()
f.write('hello \n')
f.write('world \n')
f.write(',hoorayitt')
print(f.getvalue())

from io import BytesIO
f = BytesIO()
f.write('中文,汉字 \n'.encode('utf-8'))
print(f.getvalue())
print(f.getvalue().decode('utf-8'))



#===============================================================
#    TITLE: 操作目录和文件
#===============================================================

import os

print('\n'.join(dir(os)))
print("=============================")
print(os.path.abspath('.')) # 打印绝对路径
print(os.path.join('.', 'testdir'))

with open('./tst.py','w') as f:
    f.write('hello')
if not os.path.exists('./testdir'):
    print(os.mkdir('./testdir'))
# print(os.rmdir('./testdir'))
print(os.rename('./tst.py','./tst2.py'))
print(os.path.split('/Users/iff/pySpree/PY_notes/testdir/file.txt'))
print(os.path.splitext('/Users/iff/pySpree/PY_notes/testdir/file.txt'))
with open('./tst.py','w') as f:
    f.write('hello')
print(os.remove('tst.py'))

#===============================================================
# NOTE: 文件路径操作
#===============================================================
path = './testdir_'


os.mkdir(path)
# os.remove(path)
# os.mkdir(path)
os.unlink(path)  # 删除指定路径的文件。路径可以是全名，也可以是当前工作目录下的路径。
os.removedirs # 删除文件，并删除中间路径中的空文件夹
os.chdir(path) # 将当前工作目录改变为指定的路径
os.getcwd() # 返回当前的工作目录
os.curdir # 表示当前目录的符号
# os.rename(old, new) # 重命名文件
# os.renames(old, new) # 重命名文件，如果中间路径的文件夹不存在，则创建文件夹
os.listdir(path) # 返回给定目录下的所有文件夹和文件名，不包括 '.' 和 '..' 以及子文件夹下的目录。（'.' 和 '..' 分别指当前目录和父目录）
os.mkdir(name) # 产生新文件夹
os.makedirs(name) # 产生新文件夹，如果中间路径的文件夹不存在，则创建文件夹
# 测试
os.path.isfile(path)  # 检测一个路径是否为普通文件
os.path.isdir(path) # 检测一个路径是否为文件夹
os.path.exists(path) # 检测路径是否存在
os.path.isabs(path) # 检测路径是否为绝对路径
# split 和 join
os.path.split(path) # 拆分一个路径为 (head, tail) 两部分
os.path.join(a, *p) # 使用系统的路径分隔符，将各个部分合成一个路径
# 其他
os.path.abspath() # 返回路径的绝对路径
os.path.dirname(path) # 返回路径中的文件夹部分
os.path.basename(path) # 返回路径中的文件部分
os.path.splitext(path) # 将路径与扩展名分开
os.path.expanduser(path) # 展开 '~' 和 '~user'
os.mkdir(path)


print("#===============================================================")
print("#    describe:  Other")
print("#===============================================================")


import pprint
data = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
    )
pprint.pprint(data)


#===============================================================
#    NOTE:  序列化和反序列化
#===============================================================


# 序 列 化:把变量或对象从内存中变成可存储或传输的过程称之为序列化 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等
# 反序列化:反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# 在Python中，有两种提供序列化的模块:

#===============================================================
#    describe:  pickle, python独有的
#===============================================================

# pickle 模块实现了一种算法，可以将任意一个 Python 对象转化为一系列的字节，也可以将这些字节重构为一个有相同特征的新对象。由于字节可以被传输或者存储，因此 pickle 事实上实现了传递或者保存 Python 对象的功能。
# cPickle 使用 C 而不是 Python 实现了相同的算法，因此速度上要比 pickle 快一些。但是它不允许用户从 pickle 派生子类。如果子类对你的使用来说无关紧要，那么 cPickle 是个更好的选择。

try:
    import cPickle as pickle
except:
    import pickle
# 序列化(三种编码格式,(0-1-2),(-1代表最高级的))
# dumps ： 直接将变量或对象序列化成bytes，可以用print打印内容
# dump   ： 写入指定的文件

# 反序列化
# loads  ： 直接将序列化后的字节流，反序列化（加载，还原）成序列化之前的状态，可以用print打印内容
# load    ： 将一个序列化后的文件反序列化（加载，还原）成变量或者对象


#===============================================================
#    describe:  json
#===============================================================
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

# JSON类型    Python类型
# -------------------
'''
{}  (无序)    dict
[]  (有序)    list
"string"      str
1234.56       int或float
true/false    True/False
null          None
'''

# 同样有dump和load的用法

# 5.5 JSON进阶-序列化类对象
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__)) #匿名函数
json_str = '{"age": 20, "score": 88, "name": "Bob"}'

# 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook=dict2student))  # 打印出的是反序列化的Student实例对象。



# 序列化对象可以为基本类型,class或者是一个包含多个同种类的列表.

# 5.6 JSON和pickle模块的区别 
# 1、JSON只能处理基本数据类型。pickle能处理所有Python的数据类型。
# 2、JSON用于各种语言之间的字符转换。pickle用于Python程序对象的持久化或者Python程序间对象网络传输，但不同版本的Python序列化可能还有差异。

# 6. glob 模块：文件模式匹配
import glob

# glob 函数支持三种格式的语法：
# * 匹配单个或多个字符
# ? 匹配任意单个字符
# [] 匹配指定范围内的字符，如：[0-9]匹配数字。
print(glob.glob("./note*[0-9]*.py"))




print("#===============================================================")
print("#    describe:  Shutil")
print("#===============================================================")
import shutil

# 拷贝文件
print(shutil.copyfile('./tst2.py','./testdir/copytst.py'))
print("copytst.py" in os.listdir('./testdir'))
# 复制文件夹
shutil.copytree("testdir/", "test_dir_copy/")
print("test_dir_copy" in os.listdir(os.curdir))

#删除非空文件夹
try:
    os.removedirs("test_dir_copy") # 不能
except Exception as msg:
    print(msg)
shutil.rmtree("test_dir_copy") # 可以

# 7.4 移动文件夹 # shutil.move 可以整体移动文件夹，与 os.rename 功能差不多。

# 7.5 产生压缩文件
# 查看支持的压缩文件格式：
shutil.get_archive_formats()

# 产生压缩文件：
# shutil.make_archive(basename, format, root_dir)
shutil.make_archive("test_archive", "zip", "testdir/")
# gzip, zipfile,tarfile等等见chapter6,6.8节

# 清理生成的文件和文件夹：
os.remove("test_archive.zip")



#===============================================================
#    describe:  读写CSV表格文件
#===============================================================


import csv

# 读
fp = open("data.csv")
data = []
with open('data.csv') as fp:
    r = csv.reader(fp)
    for row in r:
        data.append([row[0], int(row[1]), float(row[2])])# 默认都是字符串
for line in data:
    print(line)

# 写
data = [('one, \"real\" string', 1, 1.5), ('two', 2, 8.0)]
with open('out.psv', 'w') as fp:
    w = csv.writer(fp, delimiter="|")# 想写入字符串中的逗号可以更改分隔符
    w.writerows(data)


#===============================================================
# numpy.loadtxt() 和 pandas.read_csv() 可以用来读写包含很多数值数据的 csv 文件：
#===============================================================
