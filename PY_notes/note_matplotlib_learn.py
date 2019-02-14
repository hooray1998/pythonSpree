# -*- coding:utf-8 -*-

'''
#===============================================================
# NOTE:最简单的入门是从类 MATLAB API 开始，它被设计成兼容 MATLAB 绘图函数。
#===============================================================
from pylab import *
from numpy import *

# linspace表示在0到5之间用10个点表示
x = linspace(0, 5, 10)
y = x ** 2

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')

# 创建子图，选择绘图用的颜色与描点符号:
subplot(1,2,1)
#plot的第三个参数表示画线的颜色与样式
plot(x, y, 'r--')
subplot(2,2,4)
plot(y, x, 'g*-');
show()

'''
#===============================================================
# NOTE:matplotlib 面向对象 API
#===============================================================
# 使用面向对象API的方法和之前例子里的看起来很类似，不同的是，我们并不创建一个全局实例，而是将新建实例的引用保存在 fig 变量中,如果我们想在图中新建一个坐标轴实例，只需要 调用 fig 实例的 add_axes 方法

import matplotlib.pyplot as plt
from pylab import *
x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('TTTTTTitle')

#plt.show()
#===============================================================
# NOTE:我们对于图表的绘制有了完全的控制权，可以很容易地多加一个坐标轴到图中：
#===============================================================
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # insert axes

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');

#plt.show()
#===============================================================
# NOTE:如果我们不在意坐标轴在图中的排放位置️，那么就可以使用matplotlib的布局管理器了，我最喜欢的是subplots，使用方式如下：
#===============================================================

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

fig.tight_layout()
#plt.show()

#===============================================================
# NOTE:图表尺寸，长宽比 与 DPI
#===============================================================
# 在创建 Figure 对象的时候，使用figsize 与 dpi 参数能够设置图表尺寸与DPI， 创建一个800*400像素，每英寸100像素的图就可以这么做：
# fig = plt.figure(figsize=(8,4), dpi=100)


#===============================================================
# NOTE:可以使用 savefig 保存图表
#===============================================================
# 这里我们也可以有选择地指定DPI，并且选择不同的输出格式：
# fig.savefig("filename.png", dpi=200)


#===============================================================
# NOTE:标题，轴标，与图例的用法：
#===============================================================
fig, ax = plt.subplots()

ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, label="y = x**3")
ax.legend(loc=2) # upper left corner,显示图例
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title');

#plt.show()


#===============================================================
# NOTE:格式化文本，LaTeX，字体大小，字体类型
#===============================================================
# 不过这里我们会遇到一些小问题，在 LaTeX 中我们常常会用到反斜杠，比如 \alpha 来产生符号 α 。但反斜杠在 python 字符串中是有特殊含义的。为了不出错，我们需要使用原始文本，只需要在字符串的前面加个r就行了，像是 r”\alpha” 或者 r’\alpha’：
fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$', fontsize=18)
ax.set_ylabel(r'$y$', fontsize=18)
ax.set_title('title');

#plt.show()
#===============================================================
# NOTE:twinx 与 twiny 函数能设置双坐标轴：
#===============================================================

fig, ax1 = plt.subplots()

ax1.plot(x, x**2, lw=2, color="blue")
ax1.set_ylabel(r"area $(m^2)$", fontsize=16, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")

ax2 = ax1.twinx()
ax2.plot(x, x**3, lw=2, color="red")
ax2.set_ylabel(r"volume $(m^3)$", fontsize=16, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")
#plt.show()

#===============================================================
# NOTE:设置坐标原点在（0，0）点
#===============================================================
fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0

xx = np.linspace(-0.75, 1., 100)
ax.plot(xx, xx**3);
#plt.show()


#===============================================================
# NOTE:其他 2D 图表风格
#===============================================================
# 包括一般的 plot 方法, 还有很多其他函数能够生成不同类型的图表，详情请见 http://matplotlib.org/gallery.html 这里列出其中几种比较常见的函数方法。
n = array([0,1,2,3,4,5])


fig, axes = plt.subplots(1, 4, figsize=(12,3))

axes[0].scatter(xx, xx + 0.25*randn(len(xx)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5);
axes[3].set_title("fill_between");
#plt.show()

# polar plot using add_axes and polar projection
fig = plt.figure()
ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
t = linspace(0, 2 * pi, 100)
ax.plot(t, t, color='blue', lw=3);


# A histogram
n = np.random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title("Default histogram")
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title("Cumulative detailed histogram")
axes[1].set_xlim((min(n), max(n)));

plt.show()

#===============================================================
# NOTE:饼状图
#===============================================================
labels='frogs','hogs','dogs','logs'
sizes=15,20,45,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
explode=0,0.1,0,0
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()
#===============================================================
# NOTE:文本注释
#===============================================================
# text 函数可以做文本注释，且支持 LaTeX 格式：

fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)

ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green");
plt.show()
