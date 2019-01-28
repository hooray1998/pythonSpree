
print("#===============================================================")
print("#   TITLE: 4.1 describe: 函数接受不定数目的参数等等")
#    describe:
# 在 python 中，类型属于对象，变量是没有类型的：
# a=[1,2,3]
# a="Runoob"
# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。 
#===============================================================# 


# 1.3.4 接收不定参数
# 可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。
# 使用如下方法，可以使函数接受不定数目的参数：
# 其中，加了星号（*）的变量名会存放所有未命名的变量参数,相当于元组类型


#===============================================================
#    func_name:  add
#     describe:  计算多个数据的和
#===============================================================

def add(x, *args):
    "不定长参数实例"   # 传给他的  __doc__ 属性值
    total = x
    for arg in args:
        total += arg
    return total
print(add.__doc__)

# 再看这个例子，可以接收任意数目的位置参数和键值对参数：



#===============================================================
#   func_name:  foo
#    describe: 
#       不过要按顺序传入参数，先传入位置参数 args ，在传入关键词参数 kwargs 。
#       这里，*args 表示参数数目不定，可以看成一个元组，把第一个参数后面的参数当作元组中的元素。
#       这里， **kwargs 表示参数数目不定，相当于一个字典，关键词和值对应于键值对。
#===============================================================
def foo(*args, **kwargs):
    print(args, kwargs)

foo(2, 3, x='bar', z=10)



# 需加 * 号
def add(x, y):
    """Add two numbers"""
    a = x + y
    return a
    
z = (2, 3)
print(add(*z))


# 修改全局变量 需声明
gcount = 0
 

#===============================================================
#   func_name:  global_test
#    describe:
#===============================================================

def global_test():
    global  gcount
    gcount+=3
    print (gcount)
    
global_test()
print(gcount)



# 再一个例子
def scope_test():
    def do_local():
        spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
    def do_nonlocal():
        nonlocal  spam        #使用外层的spam变量
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()
    print("After global assignment:",spam)
 
scope_test()
print("In global scope:",spam)
# After local assignmane: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam


# 函数高级用法

# lambda函数


print("#===============================================================")
print("#   TITLE: 4.2 # 函数高级用法")
#    describe: lambda 
#===============================================================


lambda x,y: x if x>y else y

g = lambda x : x**2
print(g(5))

# map方法生成序列
res = map(lambda x:x**2,[1,5,7,4,8])
print(type(res))
for i in res:
        print(i)

print(res)
# python内置的一个高阶函数，它接收一个函数aFun和一个序列seq,并且把seq的元素以此传递给函数aFun，然后返回一个函数aFun处理完所有seq元素的列表
# 其用法为：
# map(aFun, aSeq)
# 将函数 aFun 应用到序列 aSeq 上的每一个元素上，返回一个列表，不管这个序列原来是什么类型。
# 事实上，根据函数参数的多少，map 可以接受多组序列，将其对应的元素作为参数传入函数

def add(x, y): 
    return x + y

a = (2,3,4)
b = [10,5,3]
result = map(add, a, b)

# 如何改写 map + lambda
a = (2,3,4)
b = [10,5,3]
list(map(lambda x,y : (x+y,x-y) , a, b))

# 2.3 reduce()函数
# reduce()函数也是python的内置高阶函数，reduce()函数接收的的参数和map()类似，一个函数aFun，一个序列seq，但行为和map()不同，reduce()传入的参数f必须接受2个参数，

# 第一次调用是把seq的前两个元素传递给aFun,第二次调用时，就是把前两个seq元素的计算结果当成第一个参数，seq的第三个元素当成第二个参数，传入aFun进行操作，以此类推，并最终返回结果；

# 简单说：reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce

def f(x,y):
    return x + y

print(reduce(f,  [1,2,3,4,5]))
# reduce()还可以接收第3个可选参数，作为计算的初始值。
print(reduce(lambda x,y : x+y,  [1,2,3,4,5], 100))


# 生成器
print("generator show~~~~~~~~~~~~")
def gen_example():
    
    print('before any yield')
    yield 'first yield'
    print('between yields')
    yield 'second yield'
    print('no yield anymore')
    
gen = gen_example()  #调用gen example方法并没有输出任何内容，说明函数体的代码尚未开始执行

# 使用generator expression生成generator
gen = (x * x for x in range(5))  #前文已经有介绍-推导式
print(gen)  

# 使用方法

# for i in range(5):
    # print(next(gen))
# for i in gen:
    # print(i)
for i in gen_example():
    print(i)
    print("loop~~")


# 2.5.4 yield返回值&&传参
# returnval = send(msg) 
# 传递参数msg给当前中断yield前面的变量
# 同时返回下一个yield后面的参数给return
# returnval = next(a) 
# 没有传递参数或者说传递参数None给当前中断yield前面的变量
# 同时返回下一个yield后面的参数给return

#生成器
def f():
    print('start')
    a = yield 1  # 可以返回参数1，并接收传递的参数给a
    print(a) 
    print('middle')
    b = yield 2  #可以返回参数2，并接收传递的参数给b
    print(b)
    print('next')
    c = yield 3  # 可以返回参数3，并接收传递的参数给c
    print(c)  # 这里貌似永远不会执行，因为总会在上一行的yield处结束

a = f() # 这里不会执行，即没有任何打印信息
# a.next()  # 这种写法在python3里面会报错
return1 = next(a)  # 输出start，中断在yield 1处，返回yield后面的1给return1
# return1 = a.send(None) #效果同上一条语句
# return1 = a.send('test') #这里会报错
#如果首次执行generator，就传递一个非None的参数，因为第一次执行不是从一般的中断yield处执行起，所以没有yield关键字来接收传参，就会报错
print(return1)
return2 = next(a)#传入参数为None，即a=None，返回2给return2
print(return2)
return3 = a.send('msg')#传入参数msg，即b=msg,返回3给return3
print(return3)
# start
# 1
# None
# middle
# 2
# msg
# next
# 3


# 偏函数
from  functools import partial  
  
def sum(*args):  
    s = 0  
    for n in args:  
        s = s + n  
    return s  
  
sum_add_10    = partial(sum,10)    #10 作用在sum第一个参数的位置  
sum_add_10_20 = partial(sum,10,20) #10 20 分别作用在sum第一个和第二个参数的位置  
sum_add_10_10 = partial(sum,10,10)
print('A____________我们看下原函数sum的函数地址入口：')  
print(sum)  
print('B______我们看下partial函数返回函数的地址入口：')  
print(partial(sum,10))  

print(sum_add_10(1,2,3,4,5))    # --> 10 + 1 + 2 + 3 + 4 + 5 = 25  
print(sum_add_10_20(1,2,3,4,5)) # --> 10 + 20 + 1 + 2 + 3 + 4 + 5 = 45  

'''
内置函数  slice(start, stop,[,step])
创建一个切片对象，作用在有序序列上
'''
L = list(range(1,11))  # 1 - 10 的有序序列

slice_5_10 = partial(slice, 5, 10)  # 新函数：返回一个切片对象，从5到10
print(L[slice_5_10()])
print(L[slice_5_10(2)])



# 装饰器

from functools import wraps  
  
def sum_add(*args1): #我们要给我们的装饰器decorator，带上参数  
    def decorator(func):  
        @wraps(func) #加上这句，原函数func被decorator作用后，函数性质不变  ————module————，__name__, __doc___
        def my_sum(*args2): #注意，参数要和原函数保持一致，真正实行扩展功能的是外层的装饰器  
            my_s = 0  
            for n in args1:  
                my_s = my_s +n #这个是我们新加的求和结果  
            print("sum",my_s)
            return func(*args2) + my_s #这个，我们在原求和函数的结果上再加上s，并返回这个值  
        return my_sum #返回my_sum函数，该函数扩展原函数的功能  
    return decorator  #返回我们的装饰器  


def t1():
    def decorator(func):
        @wraps(func)
        def my_sum(*args2):
            my_s = 1
            return func(*args2) + my_s
        return my_sum
    return decorator

def t2():
    def decorator(func):
       # @wraps(func)
        def my_sum(*args2):
            my_s = 1
            return func(*args2) + my_s
        return my_sum
    return decorator

@t2()
#@t1()
#@sum_add(10,20,4) #启用装饰器 对sum函数进行功能扩展
def sum(*args):  
    s = 0  
    for n in args:  
        s = s+n  
    return s  

print(sum(1,2,3,4,5))  
print(sum.__name__)  


#函数也是对象
def now():
    print('2018-04')

f = now
f()
now()

print(now.__name__)
print(f.__name__)

# 装饰器定义    
def log(func):  #  func = now()
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)  # 回调
    return wrapper

@log
def now():
    print('2018-04-01')

now()

f = now

print(f.__name__)
print(now.__name__)
# call now():
# 2018-04-01
# wrapper
# wrapper

# 把@log放到now()函数的定义处，相当于执行了语句：

# now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 装饰器传参
### 2.8.2 装饰器传参

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 用法如下
@log('execute')
def now():
    print('2018-04-01')

now()

#output
#execute now()
#2018-04-01
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)

# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper



# 另一个例子

#/usr/bin/env Python3  
#-*- encoding:UTF-8 -*-  
#test.py  

#===============================================================
#   func_name:  add
#    describe: 
#===============================================================

def add(*args):   
    """这是一个求和函数，参数可变(不知参数多少个)"""  
    sum = 0  
    for n in args:  
        sum = sum + n  
    return sum  
  
L = [1,2,3,4,5]  
print(add(*L))   
func_name = add.__name__  # 属性：返回 函数名   
print('函数名字：',func_name)  
func_doc  = add.__doc__   # 描述：返回 函数描述   
print('函数描述：',func_doc)  
# 15
# 函数名字： add
# 函数描述： 这是一个求和函数，参数可变(不知参数多少个)

print("#===============================================================")
print("#   TITLE: 4.3  describe: 导入module和package")
#===============================================================

# 多次import 没影响
# 只会载入一次,变量变了也不会再次加载,除非使用reload函数: from imp import reload   
# reload(mymodule)
# 1.模块的查找顺序是：内存中已经加载的模块->内置模块->sys.path路径（导入模块的环境变量）中包含的模块

# 2.当Python执行import语句时，它会在一些路径中搜索Python模块和扩展模块。可以通过sys.path查看这些路径

# 3. 从某个模块中导入多个函数,格式为：from somemodule import firstfunc, secondfunc, thirdfunc, oneVariable

# 4.引用模块时使用别名，格式为：import somemodule as othername

# 5.在导入时，Python会执行一遍模块中的所有内容。 mymoule.py 中所有的变量都被载入了当前环境中，不过要使用 mymodule.变量名的方法来查看或者修改这些变量：


#===============================================================
#    describe:   包
#===============================================================## 
# 我们可以这样组织一个package:

'''
package1/
    __init__.py
    subPack1/
        __init__.py
        module_11.py # define funcA
        module_12.py
        module_13.py
    subPack2/
        __init__.py
        module_21.py
        module_22.py

from package1.subPack1.module_11 import funcA
'''
import sys
print(sys.path) # 返回一个列表
# 增加一个包
# sys.path.append('/Users/Administrator/my_py_scripts')

# HACK: dir()函数:返回模块定义的所有名称,返回字符串列表, 不加参数则返回当前模块的所有属性
print(dir())

# 常用标准库
# - re 正则表达式
# - copy 复制
# - math, cmath 数学
# - decimal, fraction
# - sqlite3 数据库
# - os, os.path 文件系统
# - gzip, bz2, zipfile, tarfile 压缩文件
# - csv, netrc 各种文件格式
# - xml
# - htmllib
# - ftplib, socket
# - cmd 命令行
# - pdb 
# - profile, cProfile, timeit
# - collections, heapq, bisect 数据结构
# - mmap
# - threading, Queue 并行
# - multiprocessing
# - subprocess
# - pickle, cPickle
# - struct

print("#===============================================================")
print("#   TITLE: 4.4    describe:   try except 捕获异常")
#       也可以捕获具体的异常信息,详细看http://127.0.0.1:8888/notebooks/Python-Course-HK/day4-%E5%87%BD%E6%95%B0%E6%A8%A1%E5%9D%97%E4%B8%8E%E5%8C%85/04.04-exceptions.ipynb
#       finally总是会执行,如果出现异常没有被捕捉则会在抛出异常前执行,因此可以用来作为安全保证，比如确保打开的文件被关闭。
#===============================================================

import math

while True:
    try:
        # text = input('> ')
        text = 'q'
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print("1 / log10({0}) = {1}".format(x, y))
    except ValueError: # 输入不能为负值
        print("the value must be greater than 0")
    except ZeroDivisionError: # 输入不能为1, 否则除数为0
        print("the value must not be 1")
    except Exception: # 捕获所有异常
        print("unexpected error")
    finally:
        print("run finally statement")


print("#===============================================================")
print("#   TITLE: 4.5 describe: python3 所有内置函数")
print(round(3.1415926,3) )
# 数学相关
'''
~~  abs(a) : 求取绝对值。abs(-1)
max(list) : 求取list最大值。max([1,2,3])
min(list) : 求取list最小值。min([1,2,3])
sum(list) : 求取list元素的和。 sum([1,2,3]) >>> 6
~~ sorted(list) : 排序，返回排序后的list。
len(list) : list长度,len([1,2,3])
~~ divmod(a,b): 获取商和余数。 divmod(5,2) >>> (2,1)
pow(a,b) : 获取乘方数。pow(2,3) >>> 8  :  == print(2**3)
~~ round(a,b) : 获取指定位数的小数。a代表浮点数，b代表要保留的位数。round(3.1415926,2) >>> 3.14
range(a[,b]) : 生成一个a到b的数组,左闭右开。 range(1,10) >>> [1,2,3,4,5,6,7,8,9]


# 类型转化
~~ int(str) : 转换为int型。int('1') >>> 1
~~ float(int/str) : 将int型或字符型转换为浮点型。float('1') >>> 1.0
~~ str(int) : 转换为字符型。str(1) >>> '1'
~~ bool(int) : 转换为布尔类型。 str(0) >>> False str(None) >>> False
~~ bytes(str,code) : 接收一个字符串，与所要编码的格式，返回一个字节流类型。bytes('abc', 'utf-8') >>> b'abc' bytes(u'爬虫', 'utf-8') >>> b'\xe7\x88\xac\xe8\x99\xab'
list(iterable) : 转换为list。 list((1,2,3)) >>> [1,2,3]
~~ iter(iterable)： 返回一个可迭代的对象。 iter([1,2,3]) >>> <list_iterator object at 0x0000000003813B00>
dict(iterable) : 转换为dict。 dict([('a', 1), ('b', 2), ('c', 3)]) >>> {'a':1, 'b':2, 'c':3}
~~ enumerate(iterable) : 返回一个枚举对象。
tuple(iterable) : 转换为tuple。 tuple([1,2,3]) >>>(1,2,3)
set(iterable) : 转换为set。 set([1,4,2,4,3,5]) >>> {1,2,3,4,5} set({1:'a',2:'b',3:'c'}) >>> {1,2,3}
~~ hex(int) : 转换为16进制。hex(1024) >>> '0x400'
~~ oct(int) : 转换为8进制。 oct(1024) >>> '0o2000'
~~ bin(int) : 转换为2进制。 bin(1024) >>> '0b10000000000'
~~ chr(int) : 转换数字为相应ASCI码字符。 chr(65) >>> 'A'
~~ ord(str) : 转换ASCI字符为相应的数字。 ord('A') >>> 65


# 相关操作
~~ eval() : 执行一个表达式，或字符串作为运算。 eval('1+1') >>> 2
~~ exec() : 执行python语句。 exec('print("Python")') >>> Python
filter(func, iterable) : 通过判断函数fun，筛选符合条件的元素。 filter(lambda x: x>3, [1,2,3,4,5,6]) >>> <filter object at 0x0000000003813828>
map(func, *iterable) : 将func用于每个iterable对象。 map(lambda a,b: a+b, [1,2,3,4], [5,6,7]) >>> [6,8,10]
~~ zip(*iterable) : 将iterable分组合并。返回一个zip对象。 list(zip([1,2,3],[4,5,6])) >>> [(1, 4), (2, 5), (3, 6)]
~~ type()：返回一个对象的类型。
~~ id()： 返回一个对象的唯一标识值。
hash(object)：返回一个对象的hash值，具有相同值的object具有相同的hash值。 hash('python') >>> 7070808359261009780
~~ help()：调用系统内置的帮助系统。
isinstance()：判断一个对象是否为该类的一个实例。
issubclass()：判断一个类是否为另一个类的子类。
~~ globals() : 返回当前全局变量的字典。
next(iterator[, default]) : 接收一个迭代器，返回迭代器中的数值，如果设置了default，则当迭代器中的元素遍历后，输出default内容。
reversed(sequence) ： 生成一个反转序列的迭代器。 reversed('abc') >>> ['c','b','a']
'''

print(globals())


times in msec
 clock   self+sourced   self:  sourced script
 clock   elapsed:              other lines

000.008  000.008: --- VIM STARTING ---
000.120  000.112: Allocated generic buffers
000.519  000.399: locale set
000.543  000.024: GUI prepared
000.546  000.003: clipboard setup
000.556  000.010: window checked
001.119  000.563: inits 1
001.128  000.009: parsing arguments
005.129  004.001: expanding arguments
008.577  003.448: shell init
008.951  000.374: Termcap init
008.995  000.044: inits 2
011.200  002.205: init highlight
011.689  000.341  000.341: sourcing $VIM/vimrc
020.316  008.280  008.280: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
022.674  002.228  002.228: sourcing /Users/iff/.vim/autoload/plug.vim
027.422  001.871  001.871: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftoff.vim
036.994  000.025  000.025: sourcing /Users/iff/.vim/plugged/vim-fugitive/ftdetect/fugitive.vim
037.229  007.731  007.706: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
037.563  000.060  000.060: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
037.889  000.057  000.057: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/indent.vim
038.921  000.345  000.345: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
039.078  000.769  000.424: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/synload.vim
039.121  001.080  000.311: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syntax.vim
039.650  000.304  000.304: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/nosyntax.vim
040.951  000.533  000.533: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
041.134  001.213  000.680: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/synload.vim
041.180  001.947  000.430: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syntax.vim
041.780  000.030  000.030: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
042.073  000.023  000.023: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
044.591  000.767  000.767: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/pack/dist/opt/matchit/plugin/matchit.vim
044.666  002.313  001.546: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/macros/matchit.vim
045.098  000.032  000.032: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
045.485  000.032  000.032: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
046.003  000.043  000.043: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/indent.vim
046.782  000.027  000.027: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/filetype.vim
047.092  000.026  000.026: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/ftplugin.vim
048.115  000.293  000.293: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
048.985  000.285  000.285: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/syntax/syncolor.vim
053.974  005.557  005.272: sourcing /Users/iff/.vim/plugged/vim-monokai-tasty/colors/vim-monokai-tasty.vim
054.320  042.527  010.897: sourcing $HOME/.vimrc
054.332  000.264: sourcing vimrc file(s)
055.953  000.934  000.934: sourcing /Users/iff/.vim/plugged/vim-surround/plugin/surround.vim
057.161  000.947  000.947: sourcing /Users/iff/.vim/plugged/vim-rails/plugin/rails.vim
058.569  000.345  000.345: sourcing /Users/iff/.vim/plugged/nerdtree/autoload/nerdtree.vim
061.081  001.006  001.006: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/path.vim
061.479  000.249  000.249: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/menu_controller.vim
061.771  000.150  000.150: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/menu_item.vim
062.123  000.211  000.211: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/key_map.vim
062.745  000.482  000.482: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/bookmark.vim
063.358  000.429  000.429: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/tree_file_node.vim
064.393  000.872  000.872: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/tree_dir_node.vim
065.091  000.503  000.503: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/opener.vim
065.825  000.531  000.531: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/creator.vim
066.171  000.155  000.155: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/flag_set.vim
066.733  000.363  000.363: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/nerdtree.vim
067.691  000.782  000.782: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/ui.vim
068.054  000.142  000.142: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/event.vim
068.260  000.080  000.080: sourcing /Users/iff/.vim/plugged/nerdtree/lib/nerdtree/notifier.vim
068.947  000.568  000.568: sourcing /Users/iff/.vim/plugged/nerdtree/autoload/nerdtree/ui_glue.vim
072.168  000.140  000.140: sourcing /Users/iff/.vim/plugged/nerdtree/nerdtree_plugin/exec_menuitem.vim
073.115  000.876  000.876: sourcing /Users/iff/.vim/plugged/nerdtree/nerdtree_plugin/fs_menu.vim
073.255  000.063  000.063: sourcing /Users/iff/.vim/plugged/nerdtree/nerdtree_plugin/vcs.vim
073.782  016.339  008.392: sourcing /Users/iff/.vim/plugged/nerdtree/plugin/NERD_tree.vim
074.611  000.623  000.623: sourcing /Users/iff/.vim/plugged/auto-pairs/plugin/auto-pairs.vim
075.007  000.204  000.204: sourcing /Users/iff/.vim/plugged/vim-autopep8/plugin/python_autopep8.vim
081.625  006.433  006.433: sourcing /Users/iff/.vim/plugged/nerdcommenter/plugin/NERD_commenter.vim
083.894  002.042  002.042: sourcing /Users/iff/.vim/plugged/tagbar/plugin/tagbar.vim
084.755  000.168  000.168: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/init.vim
085.397  000.152  000.152: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/parts.vim
086.826  000.187  000.187: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/util.vim
086.891  002.724  002.217: sourcing /Users/iff/.vim/plugged/vim-airline/plugin/airline.vim
087.141  000.038  000.038: sourcing /Users/iff/.vim/plugged/vim-airline-themes/plugin/airline-themes.vim
090.150  002.812  002.812: sourcing /Users/iff/.vim/plugged/emmet-vim/plugin/emmet.vim
090.848  000.488  000.488: sourcing /Users/iff/.vim/plugged/FixedTaskList.vim/plugin/tasklist.vim
091.526  000.036  000.036: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/autoloclist.vim
091.628  000.029  000.029: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/balloons.vim
091.727  000.029  000.029: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/checker.vim
091.826  000.029  000.029: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/cursor.vim
091.927  000.030  000.030: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/highlighting.vim
092.027  000.030  000.030: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/loclist.vim
092.126  000.030  000.030: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/modemap.vim
092.235  000.033  000.033: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/notifiers.vim
092.345  000.034  000.034: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/registry.vim
092.455  000.034  000.034: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/signs.vim
094.093  001.202  001.202: sourcing /Users/iff/.vim/plugged/syntastic/autoload/syntastic/util.vim
110.046  000.249  000.249: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/autoloclist.vim
110.412  000.209  000.209: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/balloons.vim
111.228  000.714  000.714: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/checker.vim
111.647  000.314  000.314: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/cursor.vim
111.949  000.193  000.193: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/highlighting.vim
112.859  000.833  000.833: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/loclist.vim
113.210  000.270  000.270: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/modemap.vim
113.654  000.319  000.319: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/notifiers.vim
114.266  000.506  000.506: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/registry.vim
114.499  000.149  000.149: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic/signs.vim
115.817  023.287  018.329: sourcing /Users/iff/.vim/plugged/syntastic/plugin/syntastic.vim
116.842  000.254  000.254: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter/utility.vim
117.641  000.177  000.177: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter/highlight.vim
118.609  002.536  002.105: sourcing /Users/iff/.vim/plugged/vim-gitgutter/plugin/gitgutter.vim
119.674  000.848  000.848: sourcing /Users/iff/.vim/plugged/vim-fugitive/plugin/fugitive.vim
121.001  001.063  001.063: sourcing /Users/iff/.fzf/plugin/fzf.vim
122.671  001.408  001.408: sourcing /Users/iff/.vim/plugged/fzf.vim/plugin/fzf.vim
123.471  000.559  000.559: sourcing /Users/iff/.vim/plugged/YouCompleteMe/plugin/youcompleteme.vim
123.855  000.182  000.182: sourcing /Users/iff/.vim/plugged/vim-keysound/plugin/keysound.vim
124.725  000.111  000.111: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/getscriptPlugin.vim
125.096  000.284  000.284: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/gzip.vim
125.547  000.365  000.365: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/logiPat.vim
125.700  000.062  000.062: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/manpager.vim
126.051  000.267  000.267: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/matchparen.vim
126.916  000.774  000.774: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/netrwPlugin.vim
127.101  000.074  000.074: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/rrhelper.vim
127.263  000.063  000.063: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/spellfile.vim
127.592  000.236  000.236: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/tarPlugin.vim
127.850  000.161  000.161: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/tohtml.vim
128.200  000.255  000.255: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/vimballPlugin.vim
128.583  000.278  000.278: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/plugin/zipPlugin.vim
128.891  000.053  000.053: sourcing /usr/local/Cellar/macvim/8.1-153/MacVim.app/Contents/Resources/vim/runtime/pack/dist/opt/matchit/plugin/matchit.vim
128.907  007.811: loading plugins
129.085  000.178: loading packages
130.151  000.652  000.652: sourcing /Users/iff/.vim/plugged/indentLine/after/plugin/indentLine.vim
130.221  000.484: loading after plugins
130.235  000.014: inits 3
137.790  007.555: reading viminfo
137.871  000.081: setting raw mode
137.889  000.018: start termcap
137.929  000.040: clearing screen
139.231  000.576  000.576: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions.vim
139.628  000.116  000.116: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/quickfix.vim
140.135  000.313  000.313: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline.vim
140.542  000.089  000.089: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/netrw.vim
140.873  000.091  000.091: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/term.vim
141.325  000.153  000.153: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/hunks.vim
141.704  000.124  000.124: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tagbar.vim
142.375  000.375  000.375: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/branch.vim
142.789  000.113  000.113: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/fugitiveline.vim
143.182  000.107  000.107: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/syntastic.vim
143.706  000.236  000.236: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/whitespace.vim
144.290  000.129  000.129: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/po.vim
144.717  000.193  000.193: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/wordcount.vim
145.243  000.274  000.274: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline.vim
145.600  000.113  000.113: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/autoshow.vim
146.098  000.179  000.179: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/tabs.vim
146.673  000.309  000.309: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/buffers.vim
147.192  000.078  000.078: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/keymap.vim
151.838  000.157  000.157: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/section.vim
152.560  000.390  000.390: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/highlighter.vim
157.167  000.170  000.170: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/themes.vim
157.289  001.048  000.878: sourcing /Users/iff/.vim/plugged/vim-monokai-tasty/autoload/airline/themes/monokai_tasty.vim
163.750  000.605  000.605: sourcing /Users/iff/.vim/plugged/vim-monokai-tasty/autoload/airline/themes/monokai_tasty.vim
200.840  000.326  000.326: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/builder.vim
201.546  000.184  000.184: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/default.vim
229.484  000.340  000.340: sourcing /Users/iff/.vim/plugged/syntastic/autoload/syntastic/log.vim
230.252  085.705: opening buffers
233.308  000.255  000.255: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter.vim
233.606  003.099: BufEnter autocommands
233.611  000.005: editing files in windows
241.648  006.226  006.226: sourcing /Users/iff/.vim/plugged/vim-fugitive/autoload/fugitive.vim
244.241  001.069  001.069: sourcing /Users/iff/.vim/plugged/YouCompleteMe/autoload/youcompleteme.vim
386.022  145.116: VimEnter autocommands
386.037  000.015: before starting main loop
387.531  000.417  000.417: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/ctrlspace.vim
388.409  000.321  000.321: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/builder.vim
389.077  000.191  000.191: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/buflist.vim
393.624  000.146  000.146: sourcing /Users/iff/.vim/plugged/vim-airline/autoload/airline/extensions/tabline/formatters/default.vim
403.573  003.503  003.503: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar.vim
404.024  000.146  000.146: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar/debug.vim
449.189  001.231  001.231: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar/types/ctags.vim
449.667  000.122  000.122: sourcing /Users/iff/.vim/plugged/tagbar/autoload/tagbar/prototypes/typeinfo.vim
462.498  000.475  000.475: sourcing /Users/iff/.vim/plugged/vim-gitgutter/autoload/gitgutter/hunk.vim
463.507  070.918: first screen update
463.509  000.002: --- VIM STARTED ---
