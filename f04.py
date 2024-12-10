print('ada meg a másodfokú egyenlet együtthatóit: ')

a:float = float(input('a := '))
b:float = float(input('b := '))
c:float = float(input('c := '))

if a == 0:
    print('az egyenlet nem másodfokú')
else:
    d = b**2 - 4*a*c
    if d < 0: print('nincs valós megoldás')
    elif d == 0:
        print('egyetlen valós megoldás van')
        print(f'x = {-b / (2*a)}')
    else:
        print(f'x₁ = {(-b + d**.5) / (2*a)}')
        print(f'x₂ = {(-b - d**.5) / (2*a)}')