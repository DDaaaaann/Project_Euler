# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

below = 2000000
primeList = []


def find_next_prime(num):
    num += 1
    add = 1 if num % 2 == 0 else 2
    while not is_prime(num):
        num += add
    return num


def is_prime(num):
    for j in primeList:
        if not num % j:
            return False
    return True


def run():
    i = 2
    _sum = 0
    while i < below:
        primeList.append(i)
        _sum += i
        i = find_next_prime(i)
    return _sum


print run()
