# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2020/12/2 10:47
@file:1224.py
@desc:
'''

# def product(x,y=None,*args):
#     # print(x,y,args)
#     if y==None:
#         return x
#     else:
#         res=x*y
#         if args=={}:
#            return res
#         else:
#             for i in args:
#                 print(i)
#                 res=res*i
#             return res


# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
#
# move(3, 'A', 'B', 'C')

#--------------------切片test--------------------
# def trim(s):
#     while s != '' and s[0] == ' ':
#         s = s[1:]
#
#     while s != '' and s[-1] == ' ':
#         s = s[:-1]
#
#     print(s)
#     return s
#
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

#--------------------迭代test--------------------
# def findMinAndMax(L):
#     if L==[]:
#         return (None,None)
#     if len(L)==1:
#         return (L[0],L[0])
#     if len(L)==2:
#         if L[0]>L[1]:
#             return (L[1],L[0])
#         else:
#             return (L[0], L[1])
#     if len(L)>2:
#         max=1
#         min=10
#         for i in range(0,len(L)-1):
#             if L[i]>max:
#                 max=L[i]
#             if L[i]<min:
#                 min=L[i]
#         return (min,max)
#
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功！')

#--------------------列表生成式test--------------------
# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [i.lower() for i in L1 if isinstance(i, str)==True]
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

#--------------------生成器test--------------------
# def triangles():
#     t = [1]
#     while True:
#         yield t
#         t = [1] + [t[n] + t[n + 1] for n in range(len(t) - 1)] + [1]

#拆分
#n=0 t=[1] yield t  t=[1] + [t[n]+t[n+1] for n in range(1-1)] + [1]
#n=1 t=[1, 1] yield t  t=[1] + [t[n]+t[n+1] for n in range(2-1)] + [1]
#n=2 t=[1, 2, 1] yield t  t=[1] + [t[n]+t[n+1] for n in range(3-1)] + [1]  ==[1,3,3,1]

# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)
#
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

from functools import reduce
# def normalize(name):
#     return name[0].upper()+name[1:].lower()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def prod(L):
#     def res(x,y):
#         return x*y
#     return reduce(res,L)
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# def str2float(s):
#     L=s.split('.')#['123','456']
#     # print(L)
#     def char2num(r):
#         # map:接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#         # lambda x:digits[x]  ==   def fc(x):return digits[x]
#         return list(map(lambda x:digits[x],r))
#     num_list = list(map(lambda x: char2num(x), L))
#     # print(num_list)
#     int_part = reduce(lambda x,y:x*10+y, num_list[0])
#     # print(int_part)
#     float_part = reduce(lambda x,y: x*10+y, num_list[1])/10**len(num_list[1])
#     return int_part+float_part
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# def createCounter():
#     i=[0]
#     def counter():
#         i[0]+=1
#         return i[0]
#     return counter
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# -------------------------------------------------------装饰器-------------------------------------------------------
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time,functools
# def metric(fn):
#     def wrapper(*args,**kwargs):
#         # 打印开始时间和结束时间
#         starttime=time.time()
#         result = fn(*args, **kwargs)
#         endtime=time.time()
#         print('%s executed in %s ms' % (fn.__name__, endtime-starttime))
#         return result
#     return wrapper
#
# # 测试  fast=metric(fast)  slow=metric(slow)
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')


# def log(x):
#     if callable(x):
#         @functools.wraps(x)
#         def wrapper(*args,**kwargs):
#             print('call %s():' % x.__name__)
#             return x(*args, **kwargs)
#         return wrapper()
#     else:
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper1(*args,**kwargs):
#                 print('{} {}():'.format(x,func.__name__))
#                 return func(*args,**kwargs)
#             return wrapper1
#         return decorator

# @log
# def f():
#     pass

# f=log('execute')(f)
# @log('execute')
# def f():
#     pass


dict={'name':'tom'}
print(dict['name'])
print(type(dict['name']))