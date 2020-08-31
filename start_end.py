# -*- coding: UTF-8 -*-
import re
pattern =re.compile(r'\d+') # 至少匹配一个数字
m = pattern.match('one12twothree34four')

print(m)
m=pattern.match('one12twothree34four',2,10)# 从‘e’开始匹配

print (m)

m = pattern.match('one12twothree34four',3,10)  #从‘1’位置开始匹配

print ("m: ", m) 									# 返回一个Match 对象
print("group(0): ", m.group(0))

print("start(0): ",m.start(0))
print("end(0): ",m.end(0))
print("span: ",m.span(0))