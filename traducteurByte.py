import os

os.chdir('/sdcard')

a = open('bad.txt', 'r')
b = a.readlines()
for c in b :
	x= c.split()
	for line in x :
		cs = int(line)
		val = chr(cs)
		print(val , end = '')
