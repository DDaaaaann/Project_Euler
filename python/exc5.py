# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 1
_range = range(11, 21)


def is_divisible_by_range(n):
    for i in _range:
        if n % i:
            return False
    return True


while not is_divisible_by_range(num):
    num += 1

print("Smallest positive number divisible by the numbers from 1 to 20" + str(num))
