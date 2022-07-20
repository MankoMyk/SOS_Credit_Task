# Task #3.
# Описание Написать отдельный скрипт, принимающий из командной строки число, количество последних строчек, которые нужно прочесть из файла и вывести в консоль. Напишите предварительно отдельный скрипт, который генерирует текстовый файл и наполняет его случайными числами. Количество строк передается из командной строки


import random

# Parameters: 
maxLinesQtyToGen = 20
minRandomRange = -100
maxRandomRange =  100
fileName = 'TestFile.txt'

# Generating the file: 
print('   How many lines with random numbers between {} and {} you want to generate?'.format(minRandomRange, maxRandomRange))
linesQtyToGen = 0
while linesQtyToGen not in range (1,maxLinesQtyToGen+1):
    linesQtyToGen = int(input('   Enter a natural number (up to {}): '.format(maxLinesQtyToGen)))
myFile = open(fileName, 'w+')
for i in range(1,linesQtyToGen):
    myFile.write(str(random.randint(minRandomRange, maxRandomRange)))    # use "uniform" instead of "randint" for float numbers
    myFile.write('\n')
myFile.write(str(random.randint(minRandomRange, maxRandomRange)))        # use "uniform" instead of "randint" for float numbers
myFile.close()
print('   The file {} is generated.'.format(fileName))

# Printing out thw whole file: 
shouldPrintFile = ''
while shouldPrintFile not in ['Y','y','N','n']:
    shouldPrintFile = str(input('   Would you like to print it out? (Y/N): '))
if shouldPrintFile in ['Y','y']:
    myFile = open(fileName, 'r')
    print(myFile.read())
    myFile.close()

# Reading and printing out some last lines from the file: 
myFile = open(fileName, 'r')
myLines = myFile.readlines()
linesQty = len(myLines)
print('   How many last strings you want to read from the file and print out?')
linesQtyToRead = -1
while linesQtyToRead not in range(0,linesQty+1):
    linesQtyToRead = int(input('   The file has {} strings. So enter number from 0 to {}: '.format(linesQty,linesQty)))
for i in range(-linesQtyToRead,0):
    print(myLines[i].replace('\n',''))
myFile.close()
