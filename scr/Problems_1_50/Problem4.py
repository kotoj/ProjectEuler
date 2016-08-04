__author__ = 'pawel'

# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

class Problem4:

    def largestPalindrome(self):
        return Problem4().maximum(Problem4().palindromes())

    def palindromes(self):
        list = []
        for x in range(999, 0, -1):
            for y in range(999, 0, -1):
                number = x * y
                if Problem4().isPalindrome(str(number)):
                    list.append(number)
                    break
        return list

    def isPalindrome(self, word):
        reverseWord = word[::-1]
        if word == reverseWord:
            return True
        else:
            return False

    def maximum(self, numbersArray):
        max = 0
        for x in numbersArray:
            if x > max:
                max = x
        return max

print("Largest palindrome is: {0}".format(Problem4().largestPalindrome()))
