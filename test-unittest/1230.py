# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2020/12/30 13:54
@file:1230.py
@desc:
'''

import codecs
import sys

fo=open(r'C:\Users\18358\Desktop\LogAnalyse\mtc20201119_102711_044_dec.log','r',encoding='latin')
line=fo.readlines()
subscriptList=[]
add='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
for i,j in enumerate(line):
    # print("读取的字符串是 : ", i,j)
    j=j.strip()
    if add in j:
        subscriptList.append(i)
        print(line[i+1])

print(subscriptList)
print()
fo.close()
