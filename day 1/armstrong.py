# Armstrong number is a number whose sum of individual cube numbers is equal to the number

n = 1
sum = 0
digits = [int(x) for x in str(n)]
for x in digits:
    y = pow(x, 3)
    sum = sum+y
if n == sum:
    print(f'The number is an armstrong number')
else:
    print(f'The number is not an armstrong number')
