Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def tempConv(c):
	return 9/5 * c + 32

>>> tempConv(34.5)
94.1
>>> cel = [32.3,34.5,36.1,38.2,26.7,29.8]
>>> for i in cel:
	print(tempConv(i))

	
90.13999999999999
94.1
96.98
100.76
80.06
85.64
>>> def even(x):
	return x % 2 == 0

>>> num_list = [i for i in range(50)]
>>> num_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> for i in num_list:
	print(even(i))

	
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
True
False
>>> even_list = filter(even, num_list)
>>> even_list
<filter object at 0x00000275D2E93940>
>>> even_list = list(filter(even, num_list))
>>> even_list
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> fah = list(filter(tempConv, cel))
>>> fah
[32.3, 34.5, 36.1, 38.2, 26.7, 29.8]
>>> fah = list(map(tempConv, cel))
>>> fah
[90.13999999999999, 94.1, 96.98, 100.76, 80.06, 85.64]
>>> evenList = [i for i in range(0,50) if i % 2 == 0]
>>> evenList
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> 
