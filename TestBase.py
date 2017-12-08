...
NOTE Python
...

import random
import math

1 + 2
2 > 3
#2 = 3
2 == 3

center = 50
diff = 2

centerPos = int(random.randint(1, 100) / diff)
center = center + centerPos

centerDiff = math.ceil(centerPos)
centerSine = math.sin(centerDiff)

print(center)
print(centerSine)

hello = 'hello world!'
#hello2 = 'hello world's'
hello3 = "hello world's"
hello4 = 'yes I "do"'
#hello5 = bla bla bla bli bla' blo' Bled "blood" blad
hello6 = '''bla bla bla bli bla' blo' Bled "blood" blad'''

print(hello)
#print(hello2)
print(hello3)
print(hello4)
#print(hello5)

file = input( 'File Name?' )
rad = input( 'Radius?' )
stringCenterPos = str(centerPos)

text = file + ' ' + rad + ' ' + stringCenterPos
#text1 = file + ' ' + rad + ' ' + str(CenterPos)
text2 = '{0} - {2} - {1}'.format(file, rad, stringCenterPos)
text3 = '{0} - {1} - {2}'
text4 = text3.format(file, rad, stringCenterPos)
print(text)
#print(text1)
print(text2)
print(text4)

blop = 'blabli bloble'
blop2 = '010101010101010blibli0101010101010101010'
blop3 = 'Hapus'
blop4 = blop3[0:3:1]
blop5 = blop3[2:]
print(blop.count('b'))
print(blop.upper())
print(blop.islower())
print(blop.isalpha())
print(blop.isdigit())
print(blop.index('bloble'))
#print(blop.index('pret'))
print(blop.find('pret'))
print(blop.find('bloble'))
print(blop2.strip('0'))
print(blop2.strip('01'))
print(blop2.lstrip('01'))
print(blop4)
print(blop5)

myList = [1,2,3,4,"a",'a',True,[0,9,8,7,6,5]]
myList2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(type(myList))
print(myList)
print(myList[5])
print(myList[7][1::2])
print(myList2[1][1])
#print(len(anehList))
#print('aneh')
print(len(myList))
print(2 in myList)

myList.remove(1)
print(myList)

del myList[0:2]
print(myList)

#myList = myList.append(10)
#print(myList)

myList.append(99)
print(myList)

myList = myList + [111]
print(myList)

#myList = myList + list(111)
#print(myList)

myList = myList + [1,1,1]
print(myList)

myList = myList + [[1,1,1]]
print(myList)

myList = myList + ['abc']
print(myList)

myList = myList + list('abc')
print(myList)

myList.insert(2,'HOHO')
print(myList)

myTuple = (1,2,'a','b')
print(type(myTuple))

myTuple = 1,2,'a','b'
print(type(myTuple))

#print(myTuple[0])
#myTuple[1] = 'imutable'

(a, b, c) = 1, 2 , 3
print(a)

[a, b, c] = '321'
print(a)

a = 100
b = 200
c = True
d = False

print(c and d)
print(not c)

if True:
    print('print if true')

if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a = b')

#Next