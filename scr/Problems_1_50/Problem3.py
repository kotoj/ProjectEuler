__author__ = 'pawel'

class Problem3:
    def largestPrimeFactor(self, number):
        primeFactor = 2
        while number != 1:
            if number % primeFactor == 0:
                number = number / primeFactor
            else:
                primeFactor = Problem3().nextPrimeNumber(primeFactor)
        return primeFactor


    def nextPrimeNumber(self, number):
        while True:
            number += 1
            if Problem3().isPrimeNumber(number):
                return number


    def isPrimeNumber(self, number):
        for x in range(2, number):
            if number % x == 0 :
                return False
        return True

print(Problem3().largestPrimeFactor(600851475143))
print(Problem3().isPrimeNumber(6))