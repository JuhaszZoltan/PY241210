
# print('''paradicsom  1199 Ft/Kg
# paprika     1349 Ft/Kg
# voroshagyma  289 Ft/Kg''')

# osszar:float = 0
# valasz:str = 'igen'
# while (valasz != 'nem'):
#     valasz = input('kíván valamit vásárolni?: ')
#     if valasz == 'igen':
#         termek:str = input('melyik termékből?: ')
#         alapar:int = -1
#         match (termek):
#             case 'paradicsom': alapar = 1199
#             case 'paprika': alapar = 1349
#             case 'voroshagyma': alapar = 289
#             case _: print('ilyen termék nincs!')
#         if alapar != -1:
#             suly:float = float(input(f'hany kg {termek}t szeretne?: '))
#             osszar += (alapar * suly)
# print(f'osszesen fizetendo: {round(osszar)} Ft')

kinalat = {
    'paradicsom': 1199,
    'paprika': 1349,
    'voroshagyma': 289
}
for k, v in kinalat.items(): print(f'{k:<11} {v:>4}Ft/Kg')

osszar = 0.0
while True:
    valasz = input('kíván valamit vásárolni?: ')
    if valasz == 'nem': break
    elif valasz != 'igen': continue
    termek:str = input('melyik termékből?: ')
    if termek not in kinalat.keys():
        print('nincs ilyen termék')
    else:
        suly:float = float(input(f'hany kg {termek}t szeretne?: '))
        osszar += kinalat[termek] * suly
if osszar > 0: print(f'összesen fizetendő: {round(osszar)}')
print('viszlát')