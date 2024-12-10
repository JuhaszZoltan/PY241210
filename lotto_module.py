from random import randint, shuffle
from time import sleep

tipus_db:dict[int, int] = {
    5: 90,
    6: 45,
    7: 35,
}


def sorsolas(lotto_tipus:int) -> list[int]:
    if lotto_tipus not in tipus_db.keys():
        raise Exception('nincs ilyen lottó')
    szamok:list[int] = []
    for x in range(tipus_db[lotto_tipus]): szamok.append(x+1)
    shuffle(szamok)
    sorsolt:list[int] = []
    for x in range(lotto_tipus): sorsolt.append(szamok[x])
    sorsolt.sort()
    return sorsolt


def tippek_bekerese(lotto_tipus:int) -> list[int]:
    if lotto_tipus not in tipus_db.keys():
        raise Exception('nincs ilyen lottó')
    tippek:list[int] = []
    while len(tippek) < lotto_tipus:
        t = int(input(f'{len(tippek)+1}. tipp: '))
        if t < 0 or t > tipus_db[lotto_tipus]:
            print('invalid tipp: a szelvény határain kívül esik')
        elif t in tippek:
            print('invalid tipp: ez a szám már szerepel a szelvényen')
        else: tippek.append(t)
    tippek.sort()
    return tippek


def talalatok_szama(sorsolt_szamok:list[int], tippek:list[int]) -> int:
    talalatok_szama:int = 0
    for n in sorsolt_szamok:
        if n in tippek: talalatok_szama += 1
    return talalatok_szama