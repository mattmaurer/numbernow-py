#!/usr/bin/env python3
#copyright 2020 Matt Maurer
#Licensed under GNU General Public License v3.0
#https://github.com/mattmaurer/numbernow-py

import platform
import math
import csv

#NumberNow ported to Python 3

x = 1
y = 1001
z = 0
dataArray = []

print('Welcome to Number Now')

def doCalc2(x,y,z): #main function that processes the input
	x = int(input('What number should we start at?'))
	y = int(input('How many records would you like?'))
	z = int(input('Enable zero padding? 1 or 0 please'))
	j = len(str(y))
	a=0	
	while a < y:
		if z==1:
			# if we are using zero padding, we process each number through the zero function before appending it to the array
			b = zero(a)
			dataArray.append(b)
			a = a+1
		else:
			# if not using zero padding, we append each number to the dataArray
			dataArray.append(a)
			a = a+1
			
	#print(dataArray) for debugging purposes
		
	with open('numbers.csv', 'w') as f: #here we output our processed dataArray into an actual file
		writer = csv.writer(f)
		writer.writerow (['Num'])
		
		for cell in dataArray: 
			writer.writerow ([cell])
	print(f'You generated a CSV file that has {y} entries, starting at {x} and zero padding is {z}')	
			    	
def zero(s):
	s = j2.format(s)
	return s


doCalc2(x,y,z)