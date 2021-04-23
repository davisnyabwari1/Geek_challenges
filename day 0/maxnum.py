# Given two numbers, write a Python code to find the Maximum of these two numbers.
# a.using a function[naive way]
def Maximum(num1, num2):
    if num1 > num2:
        return f'{num1} is greater than {num2}'
    elif num2 > num1:
        return f'{num2} is greater than {num1}'
    else:
        return f'{num2} is equal to {num1}'


Maximum(5, 50)
# b.using max function built in python
num1 = 20
num2 = 5
maximum = max(num1, num2)
print(maximum)
