
"""Formula to calculate compound interest annually is given by:

A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount
P is principle amount
R is the rate and
T is the time span

example
 Principle (amount): 1200
Time: 2
Rate: 5.4

"""


def compound_Interest(Principle, Rate, Time):
    Amount = Principle*(pow((1 + Rate/100), Time))
    CI = Amount-Principle
    print(CI)


compound_Interest(12000, 5.4, 2)
