Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/Oct_2017/Python_WE/Python_WE_11-12_30/CorePython_Evening/01-BasicPython/07-StringMethods.py 
Enter first name : ram
Enter last name : sharma
Hello  : ramsharma
Hello  : RAM SHARMA
Hello  : ram sharma
Hello  : Ram Sharma
>>> fname
'ram'
>>> lname
'sharma'
>>> fname = 'RaM'
>>> fname.swapcase()
'rAm'
>>> fname.islower()
False
>>> lname
'sharma'
>>> lname.islower()
True
>>> name = "Ram Sharma"
>>> name.count('a')
3
>>> len(name)
10
>>> string = "Hello world this is python programming"
>>> string.count("is")
2
>>> string = "Hello world this is python programming and this is awesome"
>>> string.count("is")
4
>>> string.count(" is ")
2
>>> string
'Hello world this is python programming and this is awesome'
>>> string.join(name)
'RHello world this is python programming and this is awesomeaHello world this is python programming and this is awesomemHello world this is python programming and this is awesome Hello world this is python programming and this is awesomeSHello world this is python programming and this is awesomehHello world this is python programming and this is awesomeaHello world this is python programming and this is awesomerHello world this is python programming and this is awesomemHello world this is python programming and this is awesomea'
>>> name
'Ram Sharma'
>>> name = 'Ram,sharma'
>>> n = name.split(',')
>>> string.join(n)
'RamHello world this is python programming and this is awesomesharma'
>>> n
['Ram', 'sharma']
>>> string.join(name)
'RHello world this is python programming and this is awesomeaHello world this is python programming and this is awesomemHello world this is python programming and this is awesome,Hello world this is python programming and this is awesomesHello world this is python programming and this is awesomehHello world this is python programming and this is awesomeaHello world this is python programming and this is awesomerHello world this is python programming and this is awesomemHello world this is python programming and this is awesomea'
>>> for i in n:
	print(i.join(string))

	
HRameRamlRamlRamoRam RamwRamoRamrRamlRamdRam RamtRamhRamiRamsRam RamiRamsRam RampRamyRamtRamhRamoRamnRam RampRamrRamoRamgRamrRamaRammRammRamiRamnRamgRam RamaRamnRamdRam RamtRamhRamiRamsRam RamiRamsRam RamaRamwRameRamsRamoRammRame
Hsharmaesharmalsharmalsharmaosharma sharmawsharmaosharmarsharmalsharmadsharma sharmatsharmahsharmaisharmassharma sharmaisharmassharma sharmapsharmaysharmatsharmahsharmaosharmansharma sharmapsharmarsharmaosharmagsharmarsharmaasharmamsharmamsharmaisharmansharmagsharma sharmaasharmansharmadsharma sharmatsharmahsharmaisharmassharma sharmaisharmassharma sharmaasharmawsharmaesharmassharmaosharmamsharmae
>>> for i in n:
	print(i)

	
Ram
sharma
>>> for i in n:
	print(string.join(i))

	
RHello world this is python programming and this is awesomeaHello world this is python programming and this is awesomem
sHello world this is python programming and this is awesomehHello world this is python programming and this is awesomeaHello world this is python programming and this is awesomerHello world this is python programming and this is awesomemHello world this is python programming and this is awesomea
>>> for i in n:
	print(n[i].join(string))

	
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    print(n[i].join(string))
TypeError: list indices must be integers or slices, not str
>>> for i in range(2):
	print(n[i].join(string))

	
HRameRamlRamlRamoRam RamwRamoRamrRamlRamdRam RamtRamhRamiRamsRam RamiRamsRam RampRamyRamtRamhRamoRamnRam RampRamrRamoRamgRamrRamaRammRammRamiRamnRamgRam RamaRamnRamdRam RamtRamhRamiRamsRam RamiRamsRam RamaRamwRameRamsRamoRammRame
Hsharmaesharmalsharmalsharmaosharma sharmawsharmaosharmarsharmalsharmadsharma sharmatsharmahsharmaisharmassharma sharmaisharmassharma sharmapsharmaysharmatsharmahsharmaosharmansharma sharmapsharmarsharmaosharmagsharmarsharmaasharmamsharmamsharmaisharmansharmagsharma sharmaasharmansharmadsharma sharmatsharmahsharmaisharmassharma sharmaisharmassharma sharmaasharmawsharmaesharmassharmaosharmamsharmae
>>> n[0]
'Ram'
>>> 
