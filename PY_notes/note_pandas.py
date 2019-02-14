# coding: utf-8
# # Series和DataFrame对象的创建
#     
# pandas中的核心对象是Series和DataFrame，这一节主要介绍如何创建这两种对象。
#     Pandas 有两种自己独有的基本数据结构，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以，Python 中有的数据类型在这里依然适用，也同样还可以使用类自己定义数据类型。只不过，Pandas 里面又定义了两种数据类型：Series 和 DataFrame，它们让数据操作更简单了
get_ipython().system('cd')
import numpy as np
from pandas import Series, DataFrame
import pandas as pd
# ---
# # 1. Series
# Series是pandas中暴露给我们使用的基本对象，Series 是一个类数组的数据结构，同时带有标签（lable）或者说索引（index），同时具有列表和字典的属性（字典的属性由索引赋予）。
# 
#     Series：有序，有索引
#     list：  有序，无索引
#     dict：  无序，有索引
#     
#     比如这样一个列表：[9, 3, 8]，如果跟索引值写到一起，就是：
#     data	9	3	8
#     index   0	1	2
#     不过，在有些时候，需要把它竖过来表示
#     index	data
#         0	9
#         1	3
#         2	8
#     Series 就是“竖起来”的 list
# ## 1.1 预览
data = [1,2,3]
index = ['a','b','c']  #指定索引值
s = pd.Series(data=data, index=index, name = 'sss')
s
s[1]
s['b']
s2 = Series(["100", "Python", "C++", "3.1415"])  #未指定索引，默认0，1，2，3
s2
s.index  # 四个属性之一：索引（字典的key）
s.name  # 四个属性之二：名字，
s.values # 四个属性之三：值
s.dtype # 四个属性之四：元素类型  问题？s2.dtype
s2.dtype
s2.index
# - 列表的索引只能是从 0 开始的整数，Series 数据类型在默认情况下，其索引也是如此。
# - 不过，区别于列表的是，Series 可以自定义索引
# ----
# ## 1.2 创建
# `pd.Series(data=None, index=None, name = None)`
# - data：多种类型，见下面具体介绍
# - index：索引
# - name：对data的说明，用的不多，一般在和DataFrame、Index互相转换时才需要。
# ### 1.2.1 data无索引
# - 如果 data 为 **ndarray(1D) 或 list(1D)**，那么其缺少 Series 需要的索引信息；
# - 如果提供 index，如果给定则必须和data长度相同；
# - 如果不提供 index，那么其将生成默认数值索引 range(0, data.shape[0])。
# data = [1,2,3]
data1 = np.array([1,2,3])
index1 = ['a','b','c']
s = pd.Series(data = data1, index = index1)
s
s2 = Series(["100", "Python", "C++", "3.1415"], index=["mark", "easy", "hard", "pi"])
s2
# ### 1.2.2 data有索引
#  - 如果 data 为 **Series 或 dict** ，那么其已经提供了 Series 需要的索引信息，所以 index 项是不需要提供的；
#  - 如果额外提供了 index 项，那么其将对当前构建的Series进行 重索引（增删）（等同于reindex操作）。
# data = pd.Series([a,b,c], index = ['a','b','c'] )
data2 = { 'a':1, 'b':2,'c':3 }
index2 = ['a','b','d']
s = pd.Series(data = data2,index = index2)
s
#s = pd.Series(data = data2)
#s
#s['a']
# 如上，index项用于从当前已有索引中匹配出相同的行，如果当前索引缺失给定的索引，则填充NaN（NaN：not a number为pandas缺失值标记）。
# ## 1.3 根据索引访问
#  - 自定义索引，的确比较有意思。就凭这个，也是必须的。
#  - 每个元素都有了索引，就可以根据索引操作元素了。还记得 list 中的操作吗？Series 中，也有类似的操作。先看简单的，根据索引查看其值和修改其值
s2 = Series(["100", "Python", "C++", "3.1415"], index=["mark", "easy", "hard", "pi"])
s2
s2["easy"]
# In[ ]:
s2[1]
# 这是不是又有点类似 dict 数据了呢？的确如此。看下面就理解了。
# 前面定义 Series 对象的时候，用的是列表，即 Series() 方法的参数中，第一个列表就是其数据值，如果需要定义 index，放在后面，依然是一个列表。
# 除了这种方法之外，还可以用下面的方法定义 Series 对象：
sd = {"python":8000, "C++":8100, "Java":4000}
s3 = Series(sd)
s3
# 现在是否理解为什么前面那个类似 dict 了？因为本来就是可以这样定义的。
# 这时候，索引依然可以自定义。Pandas 的优势在这里体现出来，如果自定义了索引，自定的索引会自动寻找原来的索引，如果一样的，就取原来索引对应的值，这个可以简称为“自动对齐”。
s4 = Series(sd, index=["Java", "python", "C++", "C#"])
s4
# 在 sd 中，只有'python':8000, 'c++':8100, 'Java':4000，没有"C#"，但是在索引参数中有，于是其它能够“自动对齐”的照搬原值，没有的那个"C#"，依然在新 Series 对象的索引中存在，并且自动为其赋值 NaN。在 Pandas 中，如果没有值，都对齐赋给 NaN。
# ## 1.4 Series运算
# ### 1.4.1 判空
pd.isnull(s4)
pd.notnull(s4)
# 此外，Series 对象也有同样的方法
s4.isnull()
# ### 1.4.2 比较
s5 = Series([3,9,4,7], index=['a', 'b', 'c', 'd'])
s5
s5 > 5
s5[s5 > 5]
# ### 1.4.3 四则运算
s5 * 5
s5 + s5
# ----
# # 2. DataFrame
# DataFrame由具有共同索引的Series按列排列构成（2D），是使用最多的对象。
# DataFrame 是一种二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式。它的竖行称之为 columns，横行跟前面的 Series 一样，称之为 index，也就是说可以通过 columns 和 index 来确定一个主句的位置
# <img src=resource/DataFrame.png style="width:509px;height:156px;float:left">
# 
# ## 2.1 预览
data = [[1,2,3],
       [4,5,6]]
index = ['a','b']
columns = ['A','B','C']
df = pd.DataFrame(data=data, index = index, columns = columns)
df
df.index  # 行索引
df.columns  # 列索引，与Series的name一个意思
df.values # 值
df.dtypes  # 这里的dtype带s，查看每列元素类型
# ----
# ## 2.2 创建
# ####  pd.DataFrame(data=None, index=None, columns=None)


df.loc['b','B'] # 返回单一值，因为两维都是单索引
df.iloc[0:2,0]  # 返回Series，如果只有一维是series
