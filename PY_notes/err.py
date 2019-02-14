# -*- coding:utf-8 -*-
import pdb


def f(s):
    n = int(s)
    pdb.set_trace()  # 运行到这里会自动暂停
    result = 10 / n
    return result


s = '0'
n = int(s)
print("tset1")
k = 2**3
pdb.set_trace()  # 运行到这里会自动暂停
f(input())
