# encoding=utf-8

"""

@author: SimmerChan

@contact: 7698590@qq.com

@file: traditional2simple.py

@time: 2017/10/27 21:35

@desc: 繁体中文转为简体中文

"""
from langconv import *


def tradition2simple(line):
    line = Converter('zh-hans').convert(line)
    return line
