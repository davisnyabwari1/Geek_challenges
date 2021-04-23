# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.
import math
number = 6


def factorial(number):

    return 1 if (number == 1 or number == 0) else number*factorial(number-1)


# print(factorial(number))


def factorial(number):
    return (math.factorial(number))


print(factorial(number))
