Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [12,11,45,'Hi']
>>> a[8]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[8]
IndexError: list index out of range
>>> a = []
>>> a.append(100)
>>> a
[100]
>>> a.append(101)
>>> a
[100, 101]
>>> a.append(109)
>>> a
[100, 101, 109]
>>> a.append('Hi', 'This', 'is', 'Python')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append('Hi', 'This', 'is', 'Python')
TypeError: append() takes exactly one argument (4 given)
>>> x = ['Hi', 'This', 'is', 'Python']
>>> a.append(x)
>>> a
[100, 101, 109, ['Hi', 'This', 'is', 'Python']]
>>> a[-1]
['Hi', 'This', 'is', 'Python']
>>> a = []
>>> for i in x:
	a.append(i)
	print(a)

	
['Hi']
['Hi', 'This']
['Hi', 'This', 'is']
['Hi', 'This', 'is', 'Python']
>>> a
['Hi', 'This', 'is', 'Python']
>>> a = [12,11,45,'Hi']
>>> for i in x:
	a.append(i)
	print(a)

	
[12, 11, 45, 'Hi', 'Hi']
[12, 11, 45, 'Hi', 'Hi', 'This']
[12, 11, 45, 'Hi', 'Hi', 'This', 'is']
[12, 11, 45, 'Hi', 'Hi', 'This', 'is', 'Python']
>>> a.insert(2, 101)
>>> a
[12, 11, 101, 45, 'Hi', 'Hi', 'This', 'is', 'Python']
>>> j = [99,98,97,96,95]
>>> a.extend(j)
>>> a
[12, 11, 101, 45, 'Hi', 'Hi', 'This', 'is', 'Python', 99, 98, 97, 96, 95]
>>> a.pop()
95
>>> a
[12, 11, 101, 45, 'Hi', 'Hi', 'This', 'is', 'Python', 99, 98, 97, 96]
>>> a.pop()
96
>>> a
[12, 11, 101, 45, 'Hi', 'Hi', 'This', 'is', 'Python', 99, 98, 97]
>>> a.pop(5)
'Hi'
>>> a
[12, 11, 101, 45, 'Hi', 'This', 'is', 'Python', 99, 98, 97]
>>> a.remove('Python')
>>> a
[12, 11, 101, 45, 'Hi', 'This', 'is', 99, 98, 97]
>>> a.index('Hi')
4
>>> a.append('Hi')
>>> a
[12, 11, 101, 45, 'Hi', 'This', 'is', 99, 98, 97, 'Hi']
>>> a.remove('Hi')
>>> a
[12, 11, 101, 45, 'This', 'is', 99, 98, 97, 'Hi']
>>> a.append('Hi')
>>> a
[12, 11, 101, 45, 'This', 'is', 99, 98, 97, 'Hi', 'Hi']
>>> a.append('Hi')
>>> a.append('Hi')
>>> a
[12, 11, 101, 45, 'This', 'is', 99, 98, 97, 'Hi', 'Hi', 'Hi', 'Hi']
>>> for i in a:
	a.remove('Hi')

	
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    a.remove('Hi')
ValueError: list.remove(x): x not in list
>>> a
[12, 11, 101, 45, 'This', 'is', 99, 98, 97]
>>> for i in a:
	a.remove('Hi')
	break

Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    a.remove('Hi')
ValueError: list.remove(x): x not in list
>>> a
[12, 11, 101, 45, 'This', 'is', 99, 98, 97]
>>> max(a)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    max(a)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> a = [12,45,11,7,9,34,4,100,91]
>>> max(a)
100
>>> min(a)
4
>>> sorted(a)
[4, 7, 9, 11, 12, 34, 45, 91, 100]
>>> sorted(a, reverse = True)
[100, 91, 45, 34, 12, 11, 9, 7, 4]
>>> a
[12, 45, 11, 7, 9, 34, 4, 100, 91]
>>> a.sort()
>>> a
[4, 7, 9, 11, 12, 34, 45, 91, 100]
>>> sum(a)
313
>>> type(10.5)
<class 'float'>
>>> a.count(12)
1
>>> a.index(12)
4
>>> a.reverse()
>>> a
[100, 91, 45, 34, 12, 11, 9, 7, 4]
>>> 
