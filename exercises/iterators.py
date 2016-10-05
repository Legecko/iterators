from math import floor, sqrt, factorial
from itertools import permutations
"""Övningar på iterators."""


class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    def __init__(self):
        self.cubes = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cubes += 1
        return self.cubes ** 3


class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    def __init__(self):
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.number += 1
            if Primes._is_prime(self.number) == True:
                return self.number

    @staticmethod
    def _is_prime(x):
        root = floor(sqrt(x))
        i = 2
        while i <= root:
            if x % i == 0:
                return False
            i += 1
        return True


class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        self.number = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.number) < 2:
            """skickar siffran 0"""
            self.number.append(len(self.number))
            """skickar siffran 1 (sista i listan)"""
            return self.number[-1]
        self.number = self.number[1], self.number[0] + self.number[1]
        return self.number[1]


class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    def __init__(self):
        self.nameList = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het', 'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem',
        'Nun', 'Samekh', 'Ayin', 'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        try:
            return self.nameList[self.idx]
        except IndexError:
            raise StopIteration


class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    def __init__(self, string):
        self.original = list(string)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= factorial(len(self.original)):
            raise StopIteration
        self.i += 1

        i = -1
        k = -2
#        for letter in self.original:
        self.original[k], self.original[i] = self.original[i], self.original[k]
        self.original = self.original[k+1::-1]
        return ''.join(self.original)

    @staticmethod
    def permute(original):
       words = []
       words.append(original)
       i = -1
       k = -2
       for letter in original:
           original[k], original[i] = original[i], original[k]
           original = original[k+1::-1]
           words.append(original)
           return words



class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    pass
