# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:21:24 2019

@author: Allen
"""
class A(object):
    va = 10
    
    def foo(self):
        print (A.va)        #类变量
        print (self.va)     #实列变量
        
        self.va = 40        #实例变量
        print (A.va)        #在类的内部和外部，使用 【类名.类变】量
        print(self.va)      #在类的内部，用【self.变量名】，外部用【实例名.变量名】。
                            #已经变为实例变量
        
        va = 20             #局部变量
        print (va)
        
        A.va = 15           #类变量
        print (A.va)        
        
        print(self.va)      
        
obj1 = A()

obj2 = A()

obj1.foo()      #实例obj1.foo()在调用后已经修改了类变量va的值，
                #简单的说就是实例变量会屏蔽掉类变量的值，就像局部变量屏蔽掉全局变量的值一样。所以一般情况下是不将类变量作为实例变量使用的。
print ('A.va is: ', A.va)   
print ('obj1.va is:', obj1.va)
print ('obj2.va is:',obj2.va) 