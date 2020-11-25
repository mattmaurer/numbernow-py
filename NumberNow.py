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
	x = int(input('What is the starting number?'))
	y = int(input('How many records would you like?'))
	z = input('Enable zero padding? Y/N')
	
	if z=='Y' or 'y' or 'Yes' or 'yes':
		ztext = 'On'
	else:
		ztext = 'Off'
		
	j = len(str(y))
	a=x+y
	o=x
	while x < a:
		if z=='Y' or 'y' or 'Yes' or 'yes':
			# if we are using zero padding, we process each number through the zero function before appending it to the array
			b = str(x)
			b = b.zfill(j)
			dataArray.append(b)
			x = x+1
		else:
			# if not using zero padding, we append each number to the dataArray
			dataArray.append(x)
			x = x+1
			
	#print(dataArray) for debugging purposes
		
	with open('numbers.csv', 'w') as f: #here we output our processed dataArray into an actual file
		writer = csv.writer(f)
		writer.writerow (['Num'])
		
		for cell in dataArray: 
			writer.writerow ([cell])
	print(f'You generated a CSV file that has {y} entries, starting at {o} and zero padding is {ztext}')


doCalc2(x,y,z)