animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
print(animals)

print(animals['c'])
print(len(animals))
animals['a'] = 'anteater'
print(animals['a'])
print(len(animals['a']))
print(animals.has_key('baboon'))
print('donkey' in animals.values())
print(animals.has_key('b'))
print(animals.keys())
del animals['b']
print(len(animals))
print(animals.values())