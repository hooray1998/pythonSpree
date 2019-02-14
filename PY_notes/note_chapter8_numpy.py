# -*- coding:utf-8 -*-

#===============================================================
#    describe:  8.1
#===============================================================

from numpy import *
import matplotlib.pyplot as plt

a = [1,2,3,4]
b = [[1,2,3,4]]
a = array(a)
a = array(b)
print(a)
print(b)

print(a+1) # 所有元素加1
print(a*2) # 所有元素乘2
print(a*a) # 对应元素乘

# 元素访问
a[0]
a[:2]
a[:-2]

# 形状修改
print(a.shape)
print(a)
a.shape = 2,2
print(a)
a.shape = 4,1
print(a)
a.shape = 1,4
print(a)

# 绘图
import matplotlib
a = linspace(0, 2*pi, 21) #等差数列
print(a)
b = sin(a)
plt.plot(a,b)
# plt.show()

# 从数组中选择元素
mask = b>=0
print(mask)
plt.plot(a[mask],b[mask], 'ro')
plt.show()


#===============================================================
#    describe:  8.2
#===============================================================


a = arange(10)
plt.plot(a,a*1.5,a,a*2.5,a,a*3.5,a,a*4.5)
plt.show()
