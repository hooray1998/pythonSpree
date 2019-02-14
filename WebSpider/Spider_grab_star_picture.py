# -*- coding:utf-8 -*-
"""
Created on Mon Oct 16 20:32:27 2017
@author: 望
@modify: 非
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


# 获得源码text中各相册的(url,alt)
# 返回列表
def getPageUrls(text, name):
    re_pageUrl = r'href="(.+)">\s*<img src="(.+)" alt="' + name
    return re.findall(re_pageUrl, text)


'''
<a target="_blank" href="http://www.win4000.com/meinv155020.html">
    <img src="http://pic1.win4000.com/pic/8/b2/b244f3b468_250_300.jpg" alt="范冰冰短发西装俊美中性写真图片" title="范冰冰短发西装俊美中性写真图片">
    <p>范冰冰短发西装俊美中性写真图片</p>
</a>
'''


# 下载明星当前页面所有相册
def downPictures(text, root, name, namePinYin):
    pageUrls = getPageUrls(text, name)
    titles = re.findall(r'alt="' + name + r'(.+)" ',
                        text)  # 获得源码text中各相册的title, 上例中会匹配"短发西装俊美中性写真图片"
    all_cnt = 1
    for i in range(len(pageUrls)):
        if all_cnt > 20:
            break
        # print(pageUrls[i])
        # print(titles[i])
        # return
        pageUrl = pageUrls[i][0]  # 元组中第一个元素为相册url, 第二个为相册封面图片
        path = root + "/" # "./pics/fanbingbing/"
        # path = root + titles[i]+ "/" # 分相册存
        if not os.path.exists(path):
            os.mkdir(path)
        # if not os.listdir(path):  # 如果当前目录是新建立的（空的)
        pageText = getHTMLText(pageUrl)
        totalPics = int(re.findall(r'<em>(.+)</em>）',
                                   pageText)[0])  #  当前相册总页数
        downUrl = re.findall(r'href="(.+?)" class="">下载图片',
                             pageText)[0]  # 图片的URL
        cnt = 1
        while(cnt<=totalPics):
            if all_cnt > 20:
                break
            picPath = path + name + '__'+ namePinYin + '__' + str(all_cnt) + ".jpg"
            r = requests.get(downUrl)
            with open(picPath, 'wb') as f:
                f.write(r.content)
                f.close()
            print('{} - 第{}张下载已完成\n'.format(titles[i], cnt))
            cnt += 1
            all_cnt+=1
            nextPageUrl = re.findall(r'href="(.+?)">下一张', pageText)[0]
            pageText = getHTMLText(nextPageUrl)
            downUrl = re.findall(r'href="(.+?)" class="">下载图片',
                                 pageText)[0]
    return


def main():
    # name = input("请输入你喜欢的明星的名字:")
    # nameUrl = "http://www.win4000.com/mt/" + ''.join(
    # lazy_pinyin(name)) + ".html"
    rootUrl = "http://www.win4000.com"
    starUrl = rootUrl + "/mt/star_0_0_1.html"
    starText = getHTMLText(starUrl)
    # print(starText)
    # <a href="/mt/zhaoliying.html"><img src="http://pic1.win4000.com/tj/2017-12-07/5a28ba185fe96.jpg"><p>赵丽颖</p></a>
    star1List = re.findall(r'a href="(.+)">.+p>(.+?)</p', starText)
# <a href="http://www.win4000.com/mt/qiushiyuan.html">
# <img alt="邱诗媛图片大全" src="http://pic1.win4000.com/cover/2019-01-07/20190107133002_95773_250_300.jpg" data-original="http://pic1.win4000.com/cover/2019-01-07/20190107133002_95773_250_300.jpg" style="display: inline;">
    # <p>邱诗媛图片大全</p>
# </a>
    # star2List = re.findall(r'a href="(.+)".*alt', starText)

    for star in star1List:
        print(star)
        try:
            nameUrl = rootUrl+star[0]
            name = star[1]
            text = getHTMLText(nameUrl)  # 获取网页源码
            if not re.findall(r'暂无(.+)!', text):  # 有他的图
                root = "./pics/" + ''.join(lazy_pinyin(name)) + "/"  # 该明星保存的根目录
                if not os.path.exists(root):
                    os.mkdir(root)
                downPictures(text, root, name, ''.join(lazy_pinyin(name)))  # 下载当前页面所有相册的图片
                try:
                    nextPage = re.findall(r'next" href="(.+)"',
                                          text)[0]  # 是否有下一页  , 0号位置是第一处匹配
                    '''
                    # 只下载第一页就够了
                    while (nextPage):  # 若非空，则继续
                        nextText = getHTMLText(nextPage)
                        downPictures(nextText, root, name)
                        nextPage = re.findall(r'next" href="(.+)"', nextText)[0]
                    '''
                except IndexError:
                    print("已全部下载完毕")
        except TypeError:
            print("不好意思，没有{}的照片".format(name))
    return


if __name__ == '__main__':
    main()
