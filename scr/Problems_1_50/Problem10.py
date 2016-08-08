# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from Problems_1_50.Primes import Primes


def sumOfPrimes(limit):
    sum = 0
    for i in range(0, limit + 1):
        if Primes().isPrimeNumber(i):
            sum = sum + i
    return sum

print(sumOfPrimes(2000000))
