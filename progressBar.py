相信很多人在写一些简单的python脚本的时候都希望能够在程序运行的过程中实现进度条的功能以便查看程序运行的速度或者进度。

我之前一直想实现这样一个东西，也查看了许多博客但是都找不到一个完美的解决方案（当然，使用progressBar这个库是个选择，但很多时候我们需要一些定制功能的时候就需要考虑自己实现，其实也挺简单的，不想看废话的可以直接跳到最后）

进度条最主要的问题就是所有字符全部在同一行，而且可以修改。

然而当执行print语句的时候，python会在打印完这个语句的同时在结尾加上’\n’，也就是换行，这就导致在控制台下一旦被print之后就无法再修改了。所以我们现在的输出就不能再使用print来完成了。

我们要使用的是来自sys库的sys.stdout.write()函数，这个函数会在控制台输出这个字符串的同时不加上任何结尾，这就意味着这个输出还没有完全结束。通过sys.stdout.flush()函数可以把输出暂时打印在控制台中（造成print的假象，我们姑且先叫这个假输出）。那么如果我们使用’r’这个转义字符（回到行首），一切看起来是不是就合理很多了呢？

也就是说：打印字符串的时候，没有加上’\n’，同时让光标回到行首，再把当前缓冲区显示出来，也就好象是print了一样，但是这时候光标还在原来的位置。

举个例子：

Python

import sys, time

for i in range(5):
    sys.stdout.write('{0}/5\r'.format(i + 1))
    sys.stdout.flush()
    time.sleep(1)
1
2
3
4
5
6
import sys, time
 
for i in range(5):
    sys.stdout.write('{0}/5\r'.format(i + 1))
    sys.stdout.flush()
    time.sleep(1)
在终端下执行这段代码就会得到简单的进度条效果。

 

接下来还需要解决两个问题：

一：清空缓冲区
有些聪明的读者可能发现，当新的字符串比之前短的时候会出现问题，比如下面这段代码：

Python

import sys, time

for i in range(5):
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
1
2
3
4
5
6
import sys, time
 
for i in range(5):
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
运行后发现结果跟我们希望的不太一样。

其实是因为已经被flush出去的字符并不会主动清空，所以只有新写入的被修改了。针对这点我目前的解决方案是先输出一波空格把之前的字符串冲掉然后重新写：

Python

import sys, time

for i in range(5):
    sys.stdout.write(' ' * 10 + '\r')
    sys.stdout.flush()
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
1
2
3
4
5
6
7
8
import sys, time
 
for i in range(5):
    sys.stdout.write(' ' * 10 + '\r')
    sys.stdout.flush()
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
二：固定底边输出
有时候我们希望在进度条加载的同时还有一些其他的输出。

我们不妨在刷新掉上一次输出之后输出所需输出的字符串，然后在假输出进度条。

采用如下代码：

Python

import sys, time

for i in range(5):
    sys.stdout.write(' ' * 10 + '\r')
    sys.stdout.flush()
    print i
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
1
2
3
4
5
6
7
8
9
import sys, time
 
for i in range(5):
    sys.stdout.write(' ' * 10 + '\r')
    sys.stdout.flush()
    print i
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
就可以完成所需任务了。

怎么样，其实原理还是挺简单的吧？

这里给出一个自己实现的类用来打印进度条：

Python

# -*- coding:utf-8 -*-

# Copyright: Lustralisk
# Author: Cedric Liu
# Date: 2015-11-08

import sys, time

class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()

bar = ProgressBar(total = 10)
for i in range(10):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
# -*- coding:utf-8 -*-
 
# Copyright: Lustralisk
# Author: Cedric Liu
# Date: 2015-11-08
 
import sys, time
 
class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
 
bar = ProgressBar(total = 10)
for i in range(10):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)
效果如下：



这样就可以方便的在一些任务中查看程序运行的进度了，比如爬虫、机器学习等并不知道要花多少时间等工作也都可以有形象的时间把握了。

如果有什么其他好的建议欢迎共同讨论～
'''
# -*- coding:utf-8 -*-
import sys, time

for i in range(5):
    sys.stdout.write('{0}/5\r'.format(i + 1))
    sys.stdout.flush()
    time.sleep(1)

for i in range(5):
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)

for i in range(5):
    sys.stdout.write(' ' * 10 + '\r')
    sys.stdout.flush()
    sys.stdout.write(str(i) * (5 - i) + '\r')
    sys.stdout.flush()
    time.sleep(1)
'''
# -*- coding:utf-8 -*-

# Copyright: Lustralisk
# Author: Cedric Liu
# Date: 2015-11-08

import sys, time

class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        # print(s)
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * int(progress) + '-' * (self.width - int(progress)) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()

bar = ProgressBar(total = 20)
for i in range(20):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)
