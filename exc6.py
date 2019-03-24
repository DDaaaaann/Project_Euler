# Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

_range = range(1, 101)
sumOfTheSquares = sum([i**2 for i in _range])
squaresOfTheSum = sum(_range)**2
print("Difference squares of the sum and sum of the squares = " + str(squaresOfTheSum - sumOfTheSquares))
