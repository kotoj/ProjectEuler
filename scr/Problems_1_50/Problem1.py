__author__ = 'pawel'

class Problem1:

    def sumMultiples3and5(self, r):

        sum = 0
        for x in range(0, r):
            if (x % 3) == 0 or (x % 5) == 0:
                sum = sum + x

        print(sum)

Problem1().sumMultiples3and5(1000)




