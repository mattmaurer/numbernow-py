#!/usr/bin/env python3
# copyright 2024 Matt Maurer
# Licensed under GNU General Public License v3.0
# https://github.com/mattmaurer/numbernow-py

import platform
import math
import csv
import tkinter as tk
from tkinter import *

# NumberNow ported to Python 3

x = 1
y = 1001
z = 0
dataArray = []

# initialize the app
nn = tk.Tk()

# set the title and the size of the main window
nn.title("NumberNow")
nn.geometry("750x750")

# configure the number of columns in the main window (2)
nn.columnconfigure(0, weight=2, pad=5)
nn.columnconfigure(1, weight=2, pad=5)

labelstart = Label(text = "Starting Number", anchor="w")
labelnum = Label(text = "Number of Records", anchor="w")
labelzp = Label(text = "Zero Padding?", anchor="w")
inputstart = tk.Entry(nn, text="Starting Number")
inputnum = tk.Entry(nn, text="Number of Records")
zeropadd = tk.Entry(nn, text="Zero Padding")
submitb1 = Button(nn, text="Generate CSV", command=lambda: docalc2(inputstart.get(), inputnum.get(), zeropadd.get()))

labelstart.grid(row=1, column=0, pady=10, padx=5)
labelnum.grid(row=1, column=1, pady=10, padx=5)
inputstart.grid(row=2, column=0, pady=10, padx=25)
inputnum.grid(row=2, column=1, pady=10, padx=25)
labelzp.grid(row=3, column=0, pady=10, padx=5)
zeropadd.grid(row=4, column=0, pady=10, padx=25)
submitb1.grid(row=4, column=1, pady=10, padx=25)

# print('Welcome to Number Now')


def docalc2(startnum, countnum, zpenabled):
    # main function that processes the input
    #x = int(input('What is the starting number?'))
    #y = int(input('How many records would you like?'))
    #z = input('Enable zero padding? Y/N')

    if zpenabled == 'Y' or 'y' or 'Yes' or 'yes':
        ztext = 'On'
    else:
        ztext = 'Off'

    startnum = int(startnum)
    countnum =int(countnum)

    j = len(str(countnum))
    a = startnum + countnum
    o = startnum
    while startnum < a:
        if zpenabled == 'Y' or 'y' or 'Yes' or 'yes':
            # if we are using zero padding, we process each number through the zero function before appending it to the array
            b = str(startnum)
            b = b.zfill(j)
            dataArray.append(b)
            startnum = startnum + 1
        else:
            # if not using zero padding, we append each number to the dataArray
            dataArray.append(startnum)
            startnum = startnum + 1

    # print(dataArray) for debugging purposes

    with open('numbers.csv', 'w') as f:  # here we output our processed dataArray into an actual file
        writer = csv.writer(f)
        writer.writerow(['Num'])

        for cell in dataArray:
            writer.writerow([cell])
    print(f'You generated a CSV file that has {countnum} entries, starting at {o} and zero padding is {ztext}')


nn.mainloop()
