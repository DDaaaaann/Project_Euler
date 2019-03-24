# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

currentPrime = 2


def find_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


def is_prime(num):
    for i in range(2, num):
        if not num % i:
            return False
    return True


for j in range(2, 10002):
    currentPrime = find_next_prime(currentPrime)

print(currentPrime)
