import sys as system


def zad1():
    zdanie = input("Podaj zdanie: ")
    lista = []
    zdanies = zdanie.split()
    lista.append(zdanies)
    print(len(zdanie.split()))

def zad2():
    system.stdout.write("Podaj trzy liczby całkowite: ")
    a = int(system.stdin.readline())
    b = int(system.stdin.readline())
    c = int(system.stdin.readline())
    x = a**b + c
    system.stdout.write(str(x))

def zad3():
    x = []
    y = []
    slowo = input("podaj słowo: ")
    for i in slowo:
        x.append(i)
        y.append(i)
    y.reverse()
    if x == y:
        print("Słowo jest palindromem")
    else:
        print("Słowo nie jest palindromem")

def zad4():
    x = abs(int(input("podaj liczbe: " )))
    if x % 2 == 0:
        print("Nie jest liczbą pierwszą")
    else:
        print("Jest liczbą pierwszą")

def zad5():
    lista = []
    for i in range(1,1001):
        counter = 0
        for j in range(1,i):
            if i % j == 0:
                counter += j
        if counter == i:
            lista.append(i)
    print(lista)

def zad6():
    lista = [2, 5.3, 2.8 , 3 , 8, 3.5]
    lista2 = []
    for i in lista:
        lista2.append(i**2)
    print(lista2)


def zad7():
    counter = 0
    lista = []
    while counter < 10:
        x = int(input("Podaj liczbę: "))
        counter += 1
        if x % 2 == 0:
            lista.append(x)
    print(lista)

def zad8():
    lista = [5,'andziak','grahy',3,7.2,'grahy', 5, 5]
    slownik = {}
    for i in lista:
        slownik[i] = lista.count(i)
    listax = []
    for i in slownik:
        if isinstance(i, str):
            listax.append(i)
    for i in listax:
        slownik.pop(i)
    print(slownik)
zad8()





