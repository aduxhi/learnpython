a = (1, 2, (1,'liming', 4), 'HI')


for i in range(len(a)):
    print(a[i])
print(type(a[0]))
print(type(a[2]))
print(type(a[3]))
print(a[2][2])
print(a[2][-1])
print(a[0:])
print(a[0:-1])
print(2 in a)
print(4 in a)
print(4 in a[2])

b = ()
b = (a[0],) +(a[1],)
print(b)
