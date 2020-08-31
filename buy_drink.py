# -*- coding: utf-8 -*-

from math import *
from random import *
from scipy.special import comb, perm

count =0
for i in range(60):

  print(i)
  
  temp =comb(100,i)*0.6**i*0.4**(100-i)
  print(temp)

  count +=temp

print(1-count)

