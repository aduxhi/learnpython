'''
类(class):用来描述具有相同属性和方法的集合

方法：类中定义的函数

类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
实例变量：在类的声名中，属性是用变量来表示的。这种变量就称为实例变量。是在类声明的内部但是在类的其他成员方法之外声明。

数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
实例化：创建一个类的实例，类的具体对象。

对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。



'''



'''
class MyClass:
	i = 12345
	def f(self):
		return "hello world"
		
x = MyClass()
print("MyClass lei de shu xing i wei :", x.i)
print("MyClass lei de fang fa wei :", x.f())
'''

'''
__init__() 实例化操作后会自动调用__init__()方法
'''
'''
class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = Complex(3.0, -4.5)

print(x.r,x.i)
'''
class people:
	#定义基本属性
	name = ""
	age = 0
	# 定义私有属性，私有属性在类的外部无法直接进行访问
	__weight = 0
	# 定义构造方法
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w
	def speak(self):
		print("%s 说：我 %d 岁。"%(self.name,self.age))
'''		
p = people("runoob", 10, 30)
p.speak()
'''
#单态继承
class student(people):
	grade = ""
	def __init__(self,n,a,w,g):
		#调用父类的函数
		people.__init__(self,n,a,w)
		self.grade = g
		
	#覆写父类的方法
	def speak(self):
		print("%s shuo: wo %d sui le, zai du %d nian ji."%(self.name,self.age,self.grade))
'''
s =student("Allen Du", 25, 66, 13)

s.speak()
'''
class speaker:
	topic = ""
	name = ""
	def __init__(self,n,t):
		self.name = n
		self. topic = t
	def speak(self):
		print("我叫 %s,我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
# 多态继承
class sample (speaker,student):
	a = ""
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n,a,w,g)
		speaker.__init__(self,n,t)

#方法名相同，默认调用的是括号中排在前面的父类方法		
test = sample("Allen",25,66,6,"Python")
test.speak()



	
