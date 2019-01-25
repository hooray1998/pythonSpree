
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


#===============================================================
#   func_name:
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


