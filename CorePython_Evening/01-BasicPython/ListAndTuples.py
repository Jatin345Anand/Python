Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 11,12,13,14,15
>>> b = 12
>>> a+b
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a+b
TypeError: can only concatenate tuple (not "int") to tuple
>>> type(a)
<class 'tuple'>
>>> a = [11,12,13,14,15]
>>> type(a)
<class 'list'>
>>> a = [11,'Hello',12.5,True]
>>> type(a)
<class 'list'>
>>> a[0]
11
>>> a[1]
'Hello'
>>> a[2]
12.5
>>> a[3]
True
>>> a[4]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[4]
IndexError: list index out of range
>>> n
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> b
12
>>> a[0] + b
23
>>> tup = (11,'Hello',12.5,True)
>>> tup[1]
'Hello'
>>> tup(0)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tup(0)
TypeError: 'tuple' object is not callable
>>> tup[1]
'Hello'
>>> a
[11, 'Hello', 12.5, True]
>>> a[0] = "Bye"
>>> a
['Bye', 'Hello', 12.5, True]
>>> tup[0] =
SyntaxError: invalid syntax
>>> tup[0] = "Bye"
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tup[0] = "Bye"
TypeError: 'tuple' object does not support item assignment
>>> a = [12,12,(11,34,45),32]
>>> a
[12, 12, (11, 34, 45), 32]
>>> a = (12,12,[11,34,4]),32)
SyntaxError: invalid syntax
>>> a = (12,12,[11,34,4],32)
>>> a
(12, 12, [11, 34, 4], 32)
>>> a = [12,12,(11,34,45),32]
>>> a
[12, 12, (11, 34, 45), 32]
>>> a[2]
(11, 34, 45)
>>> a[2][0]
11
>>> ; = "Hello"
SyntaxError: invalid syntax
>>> _ = "Hello"
>>> tup
(11, 'Hello', 12.5, True)
>>> a
[12, 12, (11, 34, 45), 32]
>>> b
12
>>> a = (12, 12, [11, 34, 45], 32)
>>> a[2]
[11, 34, 45]
>>> a[2][0] = "Hello"
>>> a
(12, 12, ['Hello', 34, 45], 32)
>>> ord('a')
97
>>> ord('A')
65
>>> ord('Z')
90
>>> ord('%')
37
>>> 
