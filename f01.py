from math import pow

n:int =  int(input('irj be egy szamot: '))
v:str =  input('irj be egy szoveget: ').lower()

# print(n**2 * f'{v.lower()} ')
# for x in range(n**2): print(v, end=' ')

for x in range(int(pow(n, 2))): print(v, end=' ')