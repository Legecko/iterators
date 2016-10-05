from math import floor, sqrt, factorial
"""Övningar på generators."""


def cubes():
    """Implementera en generator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    i = 1
    while True:
        cube = i ** 3
        i += 1
        yield cube


def primes():
    """Implementera en generator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    number = 1
    while True:
        number += 1
        if _is_prime(number) == True:
            yield number


def _is_prime(x):
    root = floor(sqrt(x))
    i = 2
    while i <= root:
        if x % i == 0:
            return False
        i += 1
    return True


def fibonacci():
    """Implementera en generator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    number = [0, 1]
    yield 0
    yield 1
    while True:
        number = number[1], number[0] + number[1]
        yield number[1]


def alphabet():
    """En generator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    nameList = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het', 'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem',
    'Nun', 'Samekh', 'Ayin', 'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']
    i = -1
    for names in nameList:
        i += 1
        yield nameList[i]

def permutations(original):
    """En generator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    original = list(original)
    amount = 0
    while amount < factorial(len(original)):
        amount += 1
        i = -1
        k = -2
        for letter in original:
            original[k], original[i] = original[i], original[k]
            original = original[k+1::-1]
            yield ''.join(original)


def look_and_say():
    """En generator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    pass
