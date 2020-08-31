# -*- coding:utf-8 -*-
import pandas as pd;
from pandas import Series, DataFrame;
oridata = pd.read_csv('air_conditioner.csv', index_col = None, encoding='gbk',)
print(oridata.head())
