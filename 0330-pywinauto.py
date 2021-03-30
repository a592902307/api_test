# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2021/3/30 13:56
@file:0330-pywinauto.py
@desc:
'''

from pywinauto import application
#创建应用程序，指定应用程序的合法backend，strat方法中指定启动的应用程序
app = application.Application(backend='uia').start('notepad.exe')

#选择窗口
wind_1=app["无标题 - 记事本"]
#获取这个窗口下所有子控件
wind_1.print_control_identifiers()

#选择控件
edit=app["无标题 - 记事本"]["edit"]

#在编辑栏输入内容
edit.type_keys("自动化")
edit.type_keys("PC自动化")
edit.type_keys("musen")

#模拟操作键盘-修改编辑框内容
from pywinauto.keyboard import send_keys
#全选
send_keys("^a")
#复制c
send_keys("^c")
#粘贴
send_keys("^v")
#TAB健
send_keys("{VK_TAB}")
# #回车
# send_keys("{VK_RETURN}")
#粘贴
send_keys("^v")

#模拟鼠标操作
from pywinauto import mouse
import time
#1-鼠标移动-move方法----move()
# for i in range(10):
#     x=10*i
#     y=10*i
#     time.sleep(0.5)
#     #移动鼠标
#     mouse.move(coords=(x,y))

#2-鼠标点击-click方法--button指定左击还是右击，coords指定鼠标点击的位置
#单击-指定位置，鼠标左击
# mouse.click(button='left',coords=(40,40))
#单击-指定位置，鼠标右击
mouse.click(button='right',coords=(40,40))
#双击
mouse.double_click(button='left',coords=(40,40))

#3-鼠标的按下与释放
#按下鼠标：press，将鼠标移动到（140，40）坐标处按下
mouse.press(button='left',coords=(140,40))

#释放鼠标：repleace,将鼠标移动到（300，40）坐标处释放
mouse.release(button='left',coords=(300,40))

#4-右键单击指定坐标
mouse.right_click(coords=(400,400))
#5-鼠标中键单击指定坐标
mouse.wheel_click(coords=(400,400))
#6-滚动鼠标
mouse.scroll(coords=(1200,300),wheel_dist=-3)

