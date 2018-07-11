Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Hello this is python"
>>> a[0]
'H'
>>> a[0:4]
'Hell'
>>> a[0:5]
'Hello'
>>> a[0:]
'Hello this is python'
>>> a[:5]
'Hello'
>>> a[5:]
' this is python'
>>> a[:]
'Hello this is python'
>>> a[0:10:2]
'Hloti'
>>> a[0:100]
'Hello this is python'
>>> a[-1]
'n'
>>> a[0:-1]
'Hello this is pytho'
>>> a
'Hello this is python'
>>> a[-1:]
'n'
>>> a[-1:-100]
''
>>> a[-1:-10]
''
>>> a[::-1]
'nohtyp si siht olleH'
>>> a[::]
'Hello this is python'
>>> 'is' in a
True
>>> 'is python' in a
True
>>> a.find('is')
8
>>> a.rfind('is')
11
>>> a.rfind('i')
11
>>> a.rfind('s')
12
>>> a[11:]
'is python'
>>> b = a[11:]
>>> b
'is python'
>>> b[::-1]
'nohtyp si'
>>> 
