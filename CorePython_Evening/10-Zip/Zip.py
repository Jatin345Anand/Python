Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = [i for i in range(1,6)]
>>> x
[1, 2, 3, 4, 5]
>>> y = ['Ram', 'Shyam', 'Ravi', 'Amit', 'Mohan']
>>> for i in x,y:
	print(i)

	
[1, 2, 3, 4, 5]
['Ram', 'Shyam', 'Ravi', 'Amit', 'Mohan']
>>> for i,j in x,y:
	print(i)
	print(j)

	
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    for i,j in x,y:
ValueError: too many values to unpack (expected 2)
>>> zip(x,y)
<zip object at 0x0000017869B46D08>
>>> list(zip(x,y))
[(1, 'Ram'), (2, 'Shyam'), (3, 'Ravi'), (4, 'Amit'), (5, 'Mohan')]
>>> z = list(zip(x,y))
>>> for i in z:
	print(i)

	
(1, 'Ram')
(2, 'Shyam')
(3, 'Ravi')
(4, 'Amit')
(5, 'Mohan')
>>> for i,j in z:
	print(i)
	print(j)

	
1
Ram
2
Shyam
3
Ravi
4
Amit
5
Mohan
>>> for i,j in z:
	print(i, j)

	
1 Ram
2 Shyam
3 Ravi
4 Amit
5 Mohan
>>> a = []
>>> a.append(100)
>>> a.append(101)
>>> a.append(102)
>>> a.append([103,104,105,106])
>>> a
[100, 101, 102, [103, 104, 105, 106]]
>>> a[-1]
[103, 104, 105, 106]
>>> import itertools
>>> itertools.chain(a)
<itertools.chain object at 0x0000017869B53780>
>>> list(itertools.chain(a))
[100, 101, 102, [103, 104, 105, 106]]
>>> list(itertools.chain.from_iterable(a))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list(itertools.chain.from_iterable(a))
TypeError: 'int' object is not iterable
>>> list(itertools.chain(a))
[100, 101, 102, [103, 104, 105, 106]]
>>> a = [[100, 101, 102,], [103, 104, 105, 106]]
>>> list(itertools.chain.from_iterable(a))
[100, 101, 102, 103, 104, 105, 106]
>>> a = [[100, 101, 102,], [103, 104, 105, 106]]
>>> a_trans = zip(*a)
>>> a_trans
<zip object at 0x0000017869B60188>
>>> for i in a_trans:
	print(i)

	
(100, 103)
(101, 104)
(102, 105)
>>> a = [[100, 101, 102,], [103, 104, 105, 106]]
>>> a = [[100,101,102],]
>>> import numpy
>>> numpy.transpose(a)
array([[100],
       [101],
       [102]])
>>> a = [[100, 101, 102,], [103, 104, 105, 106]]
>>> z = list(zip(*a))
>>> z
[(100, 103), (101, 104), (102, 105)]
>>> 
