# -*- coding:utf-8 -*-

# <div class="post-card-image" style="background-image: url(https://images.unsplash.com/photo-1507721999472-8ed4421c4af2?ixlib&#x3D;rb-0.3.5&amp;q&#x3D;80&amp;fm&#x3D;jpg&amp;crop&#x3D;entropy&amp;cs&#x3D;tinysrgb&amp;w&#x3D;1080&amp;fit&#x3D;max&amp;ixid&#x3D;eyJhcHBfaWQiOjExNzczfQ&amp;s&#x3D;77546dbfa09c42bd14d26ef016226131)"></div>
import requests
from contextlib import closing
import re
import os
import time


# 获得源码
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("")


# 获得源码text中各图片的(url)
# 返回列表
def getPageUrls(text):
    re_pageUrl = r'post-card-image.+url\((.+)\)'
    return re.findall(re_pageUrl, text)


class ProgressBar(object):
    def __init__(self,
                 title,
                 count=0.0,
                 run_status=None,
                 fin_status=None,
                 total=100.0,
                 unit='',
                 sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "【%s】%s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (
            self.title, self.status, self.count / self.chunk_size / 10.0,
            self.unit, self.seq, self.total / self.chunk_size / 10.0, self.unit
        )  # 此处的10.0跟chunk_size对应
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)


def DownloadFile(file_download_url, file_save_name):
    with closing(requests.get(file_download_url, stream=True)) as response:
        print('===>\n', file_download_url)
        chunk_size = 102400  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        progress = ProgressBar(
            file_save_name,
            total=content_size,
            unit="MB",
            chunk_size=chunk_size,
            run_status="正在下载",
            fin_status="下载完成")
        with open(file_save_name, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                progress.refresh(count=len(data))


rootUrl = "https://blog.taotao.io/"
starText = getHTMLText(rootUrl)
imglist = getPageUrls(starText)
for i, img in enumerate(imglist):
    picPath = './tao2ImgsNote/' + str(i) + '.jpg'
    DownloadFile(img, picPath)
