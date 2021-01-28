import math

def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False

resultsList = []
for i in range(100000):
    value = i + 1
    count = 0
    while value != 1:
        if isEven(value) == True:
            value = value / 2
        else:
            value = value * 3 + 1
        count = count + 1
    resultsList.append((i+1,count))

f = open('CollatzConjectureP1.txt','w')
for result in resultsList:
    f.write(str(result[0]))
    f.write(',')
    f.write(str(result[1]))
    f.write('\n')
f.close()
        
             
        
