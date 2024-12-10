a:float = float(input('[a] erteke:= '))
b:float = float(input('[b] erteke:= '))
c:float = float(input('[c] erteke:= '))

r = [a, b, c]
r.sort()
(a, b, c) = (r[0], r[1], r[2])

if a+b>c:
    print('létezik ilyen 3szög')
    if a**2 + b**2 == c**2: print('derékszögű 3szög')
    else: print('nem derékszögű 3szög')
    if a==b or b==c: print('egyenlő szárú 3szög')
    else: print('nem egyenlő szárú 3szög')
    k = a + b + c
    print(f'háromszög kerülete: {k}')
    s = k/2
    print(f'háromszög területe: {(s*(s-a)*(s-b)*(s-c))**.5}')
else: print('nem létezik ilyen 3szög')