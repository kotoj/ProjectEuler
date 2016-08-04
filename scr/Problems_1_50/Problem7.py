# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

class Problem7:

    def isPrimeNumber(self, number):
        for x in range(2, number):
            if number % x == 0:
                return False
        return True

    def nextPrimeNumber(self, number):
        while True:
            number += 1
            if Problem7().isPrimeNumber(number):
                return number

    def nThPrime(self, n):
        primeNumberCount = 1
        primeNumber = 2
        while primeNumberCount != n:
            primeNumber = Problem7().nextPrimeNumber(primeNumber)
            primeNumberCount += 1
        return primeNumber




print(Problem7().nThPrime(10001))