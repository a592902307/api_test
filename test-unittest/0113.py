# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2021/1/13 10:39
@file:0113.py
@desc:
'''

# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s %s'%(self.__name,self.__score))
#
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#
#     def set_score(self,score):
#         if 0 <= score <=100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
#
#
# bart = Student('Bart Simpson', 59)
# print(bart.get_score())
# bart.set_score(69)
# print(bart.get_score())
# print(bart._Student__score)

#--------------------访问限制--------------------
# class Student(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_name(self):
#         return self.__name
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self,gender):
#         if gender=='male' or gender=='female':
#             self.__gender = gender
#         else:
#             raise ValueError('bad gender')
#
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


#--------------------继承和多态--------------------
# class Animal(object):   #编写Animal类
#     def run(self):
#         print("Animal is running...")
#
# class Dog(Animal):  #Dog类继承Amimal类，没有run方法
#     pass
#
# class Cat(Animal):  #Cat类继承Animal类，有自己的run方法
#     def run(self):
#         print('Cat is running...')
#     pass
#
# class Car(object):  #Car类不继承，有自己的run方法
#     def run(self):
#         print('Car is running...')
#
# class Stone(object):  #Stone类不继承，也没有run方法
#     pass
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Animal())
# run_twice(Dog())
# run_twice(Cat())
# run_twice(Car())
# run_twice(Stone())


#--------------------获取对象信息--------------------
'''
一、使用type()函数
使用type()函数，可以获取任何数据的类型。如果要判断一个数据是不是函数，可以使用types模块中定义的常量，如：types.FunctionType、types.LambdaType。

二、使用isinstance()函数
isinstance函数判断的是一个对象是否是该类型或位于该类型的父类继承链上。isinstance还可以判断一个变量是否是某些类型的一种，用元组写多种类型。

三、使用dir()函数
1.如果要获得一个对象全部的属性和方法，可以使用dir（）函数。它返回一个包含 字符串的list。

2.类似“__xxx__”的属性和方法在Python中都是有特殊用途的，比如len()函数获取对象的长度。但实际上，在len函数内部它会去自动调用对象的__len__()方法，所以，你可以在类中自己设定一个__len__()方法，让len返回你想要返回的长度。

四、操作一个对象状态
如getattr() 获取、setattr() 设置 和hasattr() 有没有 方法，可以直接操作一个对象的状态。

hasattr(obj,'x') #有属性‘x’吗？
setattr(obj,'y',18) #设置一个属性‘y’，值为18.
getattr(obj,'y') #获取属性y
getattr(obj,'z',404) #获取属性z，如果不存在，就返回默认值404.
'''


#--------------------实例属性和类属性--------------------
# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count=Student.count+1
#
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

#--------------------使用__slots__--------------------
# class Student(object):
#     pass
# s=Student()
# s.name='Mike'
# print(s.name)
#
# def set_age(self,age):
#     self.age=age
#
# from types import MethodType
# s.set_age=MethodType(set_age,s)
# s.set_age(25)
# print(s.age)
#
# def set_score(self,score):
#     self.score=score
# Student.set_score=set_score

#--------------------使用@property--------------------
# class Screen(object):
#     # def __init__(self,width,height):
#     #     self._width=width
#     #     self._height=height
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         if not isinstance(value, int):
#             raise ValueError('width must be an integer')
#
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if not isinstance(value, int):
#             raise ValueError('height must be an integer')
#
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self._width * self._height
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

#--------------------使用定制类--------------------
# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
# f=Fib()
# print(f[0:5])

#--------------------使用枚举类--------------------
from enum import Enum,unique

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#     BLACK = 1
# for v in Color:
#     print(v)
# result=Color.RED is Color.GREEN
# print(result)
# print(Color(2))

# Gender = Enum('Gender',('Male','Female'))
#
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')


#----------------------------------------使用元类----------------------------------------
'''
type()函数创建class对象，传入3个参数:
1、class的名称；
2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
# from hello import Hello

# def fn(name='world'):
#     print('Hello,%s!'%name)
#
# Hello=type('Hello',(object,),dict(hello=fn()))
# h=Hello()
# h.hello()
# print(type(Hello))
# print(type(h))


# FatBoy=type("FatBoss",(),{})
# print(FatBoy)

# 使用type创建带有属性的类,添加的属性是类属性
FatBoss =type("FatBoss",(),{'hobby':"胖子老板卖槟榔"})
# print(FatBoss)
# print(FatBoss.hobby)
# print(FatBoss.__dict__)

# 第二个参数元组填写继承的父类
# 定义胖子老板的女儿类，继承胖子老板类
# FatBossGril = type("FatBossGril",(FatBoss,),{})
# print(FatBossGril.hobby)
# print(FatBossGril.__mro__)
# print(FatBossGril.__class__)

# 使用type创建带有方法的类
def sell(self):# 定义一个普通的函数，等下加入胖子老板类
    # 实例方法
    print(self.hobby)

# print(hasattr(FatBoss,'hobby'))
# FatBossGril=type('FatBossGril',(FatBoss,),{'sell':sell})
# print(hasattr(FatBossGril,'sell'))
# print(hasattr(FatBossGril,'hobby'))
# fatbossGril=FatBossGril()
# fatbossGril.sell()

# 静态方法或者类方法，静态方法不需要实例化
# @staticmethod
# def static_method():
#     print("static method...")
# FatBossGril=type('FatBossGril',(FatBoss,),{'sell':sell,'static_method':static_method})
# print(FatBossGril.static_method)
# print(FatBossGril.static_method())

# 类方法
# @classmethod
# def class_method(cls):
#     print(cls.hobby)
#
# FatBossGril=type('FatBossGril',(FatBoss,),{'sell':sell,'class_method':class_method})
# print(FatBossGril.class_method)
# print(FatBossGril.class_method())

# 如何创建自己的元类，__metaclass__ 属性
def upper_attr(class_name, class_parents, class_attr):

    # class_name 会保存类的名字 Foo
    # class_parents 会保存类的父类 object
    # class_attr 会以字典的方式保存所有的类属性

    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    print("="*30)
    for name, value in class_attr.items():
        print("name=%s and value=%s" % (name,value))  # 打印所有类属性出来
        if not name.startswith("__"):
            new_attr[name.upper()] = value
            print("name.upper()=",name.upper())
            print("value=",value)

    # 调用type来创建一个类
    return type(class_name, class_parents, new_attr)

class Foo(object, metaclass=upper_attr): # python3 与 2的写法唯一区别
    bar = 'bip'


print("="*30)
print("check Foo exist bar attr=",hasattr(Foo, 'bar'))
print("check Foo exist BAR attr=",hasattr(Foo, 'BAR'))

f = Foo()
print("print f.BAR=",f.BAR)

