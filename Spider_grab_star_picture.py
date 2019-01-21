# -*- coding:utf-8 -*-
"""
Created on Mon Oct 16 20:32:27 2017
@author: 望
"""
import requests
import re
import os
from pypinyin import pinyin, lazy_pinyin


# 获得源码
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")


# 获得所有图片
def getPageUrls(text, name):
    re_pageUrl = r'href="(.+)">\s*<img src="(.+)" alt="' + name
    return re.findall(re_pageUrl, text)


def downPictures(text, root, name):
    pageUrls = getPageUrls(text, name)
    titles = re.findall(r'alt="' + name + r'(.+)" ', text)
    for i in range(len(pageUrls)):
        pageUrl = pageUrls[i][0]
        path = root + "/"
        cnt = 1
        # path = root + titles[i]+ "/"
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.listdir(path):
            pageText = getHTMLText(pageUrl)
            totalPics = int(re.findall(r'<em>(.+)</em>）', pageText)[0])
            downUrl = re.findall(r'href="(.+?)" class="">下载图片', pageText)[0]
            # while(cnt<=totalPics):
            while (cnt <= 10):
                picPath = path + str(cnt) + ".jpg"
                r = requests.get(downUrl)
                with open(picPath, 'wb') as f:
                    f.write(r.content)
                    f.close()
                print('{} - 第{}张下载已完成\n'.format(titles[i], cnt))
                cnt += 1
                nextPageUrl = re.findall(r'href="(.+?)">下一张', pageText)[0]
                pageText = getHTMLText(nextPageUrl)
                downUrl = re.findall(r'href="(.+?)" class="">下载图片',
                                     pageText)[0]
    return


def main():
    name = input("请输入你喜欢的明星的名字:")
    nameUrl = "http://www.win4000.com/mt/" + ''.join(
        lazy_pinyin(name)) + ".html"
    try:
        text = getHTMLText(nameUrl) # 获取网页源码
        if not re.findall(r'暂无(.+)!', text): # 有他的图
            root = "./pics/" + ''.join(lazy_pinyin(name)) + "/" # 该明星保存的根目录
            if not os.path.exists(root):
                os.mkdir(root)
            downPictures(text, root, name) # 下载当前页面所有相册的图片
            try:
                nextPage = re.findall(r'next" href="(.+)"', text)[0] # 是否有下一页  , 0号位置是找到的个数
                while (nextPage):
                    nextText = getHTMLText(nextPage)
                    downPictures(nextText, root, name)
                    nextPage = re.findall(r'next" href="(.+)"', nextText)[0]
            except IndexError:
                print("已全部下载完毕")
    except TypeError:
        print("不好意思，没有{}的照片".format(name))
    return


if __name__ == '__main__':
    main()
