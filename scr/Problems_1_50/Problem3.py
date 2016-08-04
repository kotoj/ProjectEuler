__author__ = 'pawel'

# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

class Problem3:
    def largestPrimeFactor(self, number):
        primeFactor = 2
        while number != 1:
            if number % primeFactor == 0:
                number = number / primeFactor
            else:
                primeFactor = Problem3().nextPrimeNumber(primeFactor)
                x = 1
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