# -*- coding:utf-8 -*-
#===============================================================
#    describe:  绘制折线图
#===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 读取本地的csv文件,里面的数据为美国失业率数据,得到的数据为DataFrame类型
unrate = pd.read_csv('unrate.csv')
# 使用pd中的pd.to_datetime函数将DATE列的字符串类型数据转换成pd中的标准时间格式
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
# 取出前面12条样本数据
first_twelve = unrate[0:12]
# 填充数据并绘制折线图,第一个参数为x轴数据,第二个参数为y轴数据
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
# 将x轴下面文字旋转90度
plt.xticks(rotation=90)
# 设置x轴的标签
plt.xlabel('Month')
# 设置y轴的标签
plt.ylabel('Unemployment Rate')
# 设置图标名称
plt.title('Monthly Unemployment Trends, 1948')
# 显示图像
# plt.show()


#===============================================================
# 在一个区域绘制多个子图
# 有时候,需要将多张图像在一块区域显示,方便对比
#===============================================================
# 确定总绘图区宽和高分别为都是3x6
fig = plt.figure(figsize=(3, 6))
# 添加第一个子图,并且确定在总绘图区域的位置,add_subpolt(2,1,1),前两个参数参数2,1表示将总绘图区域划分为两行1列(跟矩阵表示很像)
# 第3个参数表示该子图占总区域的第一个位置.注(将总区域分成2行1列后,位置顺序从左到右,从上到下,从1开始递增, 跟正常计数方式一致)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,2,3)
# 绘制子图
ax1.plot(np.random.randint(1,5,5), np.arange(5))
ax2.plot(np.arange(10)*3, np.arange(10))
# 显示图像
# plt.show()
#===============================================================
# 在一张图中同时绘制多条曲线
# 需求:在同一张图,同时将1948到1952年的失业率展示出来,曲线使用不同的颜色区分
# 绘制5年内的失业率曲线图
#===============================================================
# 读取本地数据
unrate=pd.read_csv('UNRATE2.csv')# 此处只有两年的数据
print(unrate)
# 将字符串时间转换成pd中的时间格式
unrate['DATE']=pd.to_datetime(unrate['DATE'])
# 将年份时间转换成月份时间,并新建列存起来,因为需求需要将5年内的当年12个月内的失业率展示出来,此时再用年时间作为x轴下标就不合适了
unrate['MONTH']=unrate['DATE'].dt.month
# 设置5个颜色数组,分别表示5条曲线颜色
colors=['red','green','blue','black','yellow']
# 设置总绘图区域大小,需要在调用绘图函数之前调用才有效果
plt.figure(figsize=(10,6))
#遍历5次
for i in range(5):
    #取出当年12个月的数据
    data12=unrate[12*i:12*(i+1)]
    #x轴数据
    data_x=data12['MONTH']
    #y轴数据
    data_y=data12['VALUE']
    #当年的曲线的标签
    label=str(1948+i)
    # 绘制当年的曲线图
    plt.plot(data_x,data_y,c=colors[i],label=label)
# 设置x轴标签
plt.xlabel('MONTH')
# 设置y轴标签
plt.ylabel('unrate')
# 设置图标名称
plt.title('US-unrae,1948-1952')
# 设置曲线标签说明,loc='best'表示自己选择合适的位置来摆放
plt.legend(loc='best')
# 显示图像
plt.show()
#===============================================================
# 绘制条形图
# 直方图和条形图的区别:由于分组数据具有连续性，直方图中的各矩形通常是连续排列，而条形图则是分开排列。此外直方图的高度表示各小组内数据个数，而条形图高度表示某项目内的数据个数。
#===============================================================
# 读取电影评分数据
reviews = pd.read_csv('fandango_scores.csv')
# 取出需要展示的列名
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
# 取出需要展示的样本数据
norm_reviews = reviews[cols]
# 评分数据的列名
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
# 取出第一部电影的评分样本数据
bar_heights = norm_reviews.loc[0, num_cols].values
# 条形图的位置
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
fig, ax = plt.subplots()
# 绘制条形图,第一个参数为x轴数据,第二个参数为y轴数据,第三个参数为每个条形的宽度
ax.bar(bar_positions, bar_heights,0.5)
# 设置x轴标签的位置
ax.set_xticks(tick_positions)
# 设置x轴标签的名字和角度
ax.set_xticklabels(num_cols, rotation=45)
# 设置x轴标签
ax.set_xlabel('Rating Source')
# y轴标签
ax.set_ylabel('Average Rating')
# 标题
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
plt.show()
#===============================================================
# 绘制直方图
# 直方图一般用来统计一定范围内的数据
#===============================================================
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
# 对评分进行数量统计
fandango_distribution = norm_reviews['Fandango_Ratingvalue'].value_counts()
# 排序索引
fandango_distribution = fandango_distribution.sort_index()
imdb_distribution = norm_reviews['IMDB_norm'].value_counts()
imdb_distribution = imdb_distribution.sort_index()
fig, ax = plt.subplots()
# 绘制直方图
ax.hist(norm_reviews['Fandango_Ratingvalue'],bins=20)
plt.show()
#===============================================================
# 绘制散点图
#===============================================================
# 读取电影评分数据
norm_reviews = pd.read_csv('fandango_scores.csv')
# 取出需要展示的列名
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
# 取出需要展示的样本数据
norm_reviews = reviews[cols]
fig, ax = plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
plt.show()
#===============================================================
# 绘制盒图
# 箱形图（英文：Box-plot），又称为盒须图、盒式图、盒状图或箱线图，是一种用作显示一组数据分散情况资料的统计图。因型状如箱子而得名。在各种领域也经常被使用，常见于品质管理。不过作法相对较繁琐。它能显示出一组数据的最大值、最小值、中位数、下四分位数及上四分位数。
#===============================================================

reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
fig, ax = plt.subplots()
#绘制盒图
ax.boxplot(norm_reviews[num_cols].values)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_ylim(0,5)
plt.show()
