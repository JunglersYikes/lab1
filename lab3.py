import math
import random


def zad1a():
    r = math.pow((math.e**4 - math.log(34, 2)), (1/3))
    print(r.__round__(2))


def zad1b():
    x = math.pow(math.log(20, math.e) + math.cos(45) + math.e, (1/3))
    print(x.__round__(2))


def zad1c():
    x = math.pow(math.log(20, 3) + math.sin(45) * 5/8, (1/4))
    print(x.__round__(2))


def zad1d():
    x = math.log(23, 3) + math.pow(math.sin(34)+5, (1/3))
    print(x.__round__(2))


def zad1e():
    x = math.pow(math.log(32, 2) + math.pi + math.sin(56), (1/4))
    print(x.__round__(2))


def zad2():
    x = int(input('Podaj wysokość wieży: '))
    if x <= 10:
        for i in range(x+1):
            a = 'A'*i
            print(a)
    else:
        print("Wieża może mieć tylko wysokość do 10")


def zad3():
    x = int(input('Podaj wysokość piramidy: '))
    if x <= 10:
        for i in range(x+1):
            if i % 2 != 0:
                a = ' A' * i
                print(a.center(19))
            elif i % 2 == 0:
                a = ' A' * i
                print(a.center(20))
    else:
        print("Piarmida może mieć tylko wysokość do 10")


def zad5():
    n = int(input('Podaj ilosc wierszy i kolumn: '))
    for i in range(n+1):
        b = ''
        c = 0
        for j in range(n+1):
            a = random.randint(0, 9)
            b += '  ' + str(a)
            c += a
        print(f"{b}    Suma wiersza wynosi {c}")


zad5()
