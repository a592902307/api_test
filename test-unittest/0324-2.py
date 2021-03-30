# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2021/3/24 13:50
@file:0324-2.py
@desc:
'''

def mySort(list):
    newList=[]

    while len(list)>0:
        mindata=list[0]

        for one in list:
            if mindata>one:
                mindata=one
        newList.append(mindata)
        list.remove(mindata)
    return newList

print(mySort([1,8,9,0,2]))