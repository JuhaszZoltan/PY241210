from time import sleep
from os import system

def osszeadas (a:int, b:int) -> int:
    return a + b


def koszon(nev:str) -> str:
    return f'Hello, {nev}'


def visszaszamol(sec:int) -> None:
    for x in range(sec, 0, -1):
        print(end=f'{x}')
        for _ in range(3):
            sleep(.2)
            print(end='.')
        sleep(1)
        system('cls')