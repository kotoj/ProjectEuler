import math


class Primes:


    def nextPrimeNumber(self, number):
        while True:
            number += 1
            if Primes().isPrimeNumber(number):
                return number

    def isPrimeNumber(self, number):
        if number == 0:
            return False
        if number == 1:
            return False
        numberSqrt = math.sqrt(number)
        for x in range(2, int(numberSqrt) + 1):
            if number % x == 0:
                return False
        return True

print(Primes().isPrimeNumber(11))