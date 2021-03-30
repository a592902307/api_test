# encoding: utf-8
'''
@anthor:yh
@contact:18358482401@163.com
@time:2021/3/24 11:54
@file:config.py
@desc:
'''

import logging

logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.txt',  # 日志输出文件
                    filemode='a')  # 追加模式

if __name__ == '__main__':
    logging.info("hello")