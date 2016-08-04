# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

class Problem6:
    def sumOfSquares(self, min, max):
        sum = 0
        for x in range(min, max+1):
            sum = sum + (x*x)
        return sum

    def squareOfSum(self, min, max):
        sum = 0
        for x in range(min, max+1):
            sum = sum + x
        return sum * sum

    def differrenceBetweenSumOfSquaresAndSquareOfSum(self, min, max):
        return Problem6().squareOfSum(min, max) - Problem6().sumOfSquares(min, max)

print(Problem6().differrenceBetweenSumOfSquaresAndSquareOfSum(1, 10))

print(Problem6().differrenceBetweenSumOfSquaresAndSquareOfSum(1, 100))