from lotto_module import *

print("LOTTÓSORSOLÁS")

lt:int = int(input('milyen lottót szeretnél játszani?: '))

print('töltsd ki a szelvényt!')
szelveny = tippek_bekerese(lt)
print(f'szelvényed: {szelveny}')

sorsolt1 = sorsolas(lt)
print(f'gépi sorsolás: {sorsolt1}')
talalat = talalatok_szama(sorsolt1, szelveny)
print(f'gépi találatok száma: {talalat}')
if lt == 7:
    sorsolt2 = sorsolas(lt)
    print(f'kézi sorsolás: {sorsolt2}')
    talalat2 = talalatok_szama(sorsolt2, szelveny)
    print(f'kézi találatok száma: {talalat2}')