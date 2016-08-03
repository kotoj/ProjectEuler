__author__ = 'pawel'

class Problem2:

    def evenFibonacciNumbers(self):
        x1 = 1
        x2 = 2
        evenSum = 0
        while x1 < 4000000:
            if x1 % 2 == 1:
                evenSum = evenSum + x1
            tmp = x2 + x1
            x1 = x2
            x2 = tmp
        print(evenSum)


Problem2().evenFibonacciNumbers()






