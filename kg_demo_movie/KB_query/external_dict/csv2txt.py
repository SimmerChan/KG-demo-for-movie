# encoding=utf-8

"""

@author: SimmerChan

@contact: hsl7698590@gmail.com

@file: jena_sparql_endpoint.py

@time: 2017/12/20 17:42

@desc:
把从mysql导出的csv文件按照jieba外部词典的格式转为txt文件。
nz代表专名，本demo主要指电影名称。
nr代表人名。

"""
import pandas as pd

df = pd.read_csv('./movie_title.csv')
title = df['movie_title'].values

with open('./movie_title.txt', 'a') as f:
    for t in title[1:]:
        f.write(t + ' ' + 'nz' + '\n')
