# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

class Problem5:
    def smallestPositiveEvenlyDivisible(self, min, max):
        number = max
        evenlyDivisible = False
        while True:
            for x in range(min, max+1):
                if (number % x == 0):
                    evenlyDivisible = True
                else:
                    evenlyDivisible = False
                    break
            if evenlyDivisible:
                break
            else:
                number +=1
        return number

print(Problem5().smallestPositiveEvenlyDivisible(1, 20))