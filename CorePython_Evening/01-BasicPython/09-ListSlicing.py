Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,11,100,99,'Hi','Hello',101]
>>> a[0]
12
>>> a[-1]
101
>>> a[0:5]
[12, 11, 100, 99, 'Hi']
>>> a[5:]
['Hello', 101]
>>> b = a
>>> b
[12, 11, 100, 99, 'Hi', 'Hello', 101]
>>> a
[12, 11, 100, 99, 'Hi', 'Hello', 101]
>>> b[0] = 'Python'
>>> b
['Python', 11, 100, 99, 'Hi', 'Hello', 101]
>>> a
['Python', 11, 100, 99, 'Hi', 'Hello', 101]
>>> id(a)
1826964843656
>>> id(b)
1826964843656
>>> c = a[:]
>>> c
['Python', 11, 100, 99, 'Hi', 'Hello', 101]
>>> a
['Python', 11, 100, 99, 'Hi', 'Hello', 101]
>>> c[0] = 'Bye'
>>> c
['Bye', 11, 100, 99, 'Hi', 'Hello', 101]
>>> a
['Python', 11, 100, 99, 'Hi', 'Hello', 101]
>>> id(a)
1826964843656
>>> id(c)
1826964843400
>>> a
['Python', 11, 100, 99, 'Hi', 'Hello', 101]
>>> a = ['Python', 11, 100, 99, ['Hi', 'Hello', 101],12,22]
>>> a[4][0]
'Hi'
>>> d = a
>>> d
['Python', 11, 100, 99, ['Hi', 'Hello', 101], 12, 22]
>>> d = a[:]
>>> d
['Python', 11, 100, 99, ['Hi', 'Hello', 101], 12, 22]
>>> a
['Python', 11, 100, 99, ['Hi', 'Hello', 101], 12, 22]
>>> a[4][0] = 'Bye'
>>> a
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> d
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> a[-1] = 50
>>> a
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 50]
>>> d
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> a[4]
['Bye', 'Hello', 101]
>>> a[4] = 'Something'
>>> a
['Python', 11, 100, 99, 'Something', 12, 50]
>>> d
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> import copy
>>> e = copy.deepcopy(a)
>>> e
['Python', 11, 100, 99, 'Something', 12, 50]
>>> a = ['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> e = copy.deepcopy(a)
>>> a
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> e
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> a[4][0] = 111
>>> a
['Python', 11, 100, 99, [111, 'Hello', 101], 12, 22]
>>> e
['Python', 11, 100, 99, ['Bye', 'Hello', 101], 12, 22]
>>> len(a)
7
>>> a.count(11)
1
>>> 
