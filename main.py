from module import *

nev = input('hogy hívnak?: ')

visszaszamol(3)

print(koszon(nev))

print('írj be 2 számot:')
x:int = int(input('egyik: '))
y:int = int(input('másik: '))

osszeg = osszeadas(x, y)
print(f'a két szám összege: {osszeg}')