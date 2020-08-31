#!/usr/bin/python

test = {'2','1','3'}
s = 'a'
print(s.join(test))

test = {'python', 'java', 'ruby'}

s = '->->'
print(s.join(test))

test = {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test = {1:'mat', 2:'that'}
s = ', '
print(s.join(test))