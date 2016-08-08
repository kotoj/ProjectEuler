# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,#
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

class Problem9:
    def abc(self):
        answA = 0
        answB = 0
        answC = 0

        for a in range (1, 999):
            for b in range (1, 999):
                c = 1000 - a - b
                if a*a + b*b == c*c:
                    answA = a
                    answB = b
                    answC = c
                    print("a: {0}, b: {1}, c: {2}".format(answA, answB, answC))
                    return a * b * c



print(Problem9().abc());
