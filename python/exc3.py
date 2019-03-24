# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143
currentPrime = 2
largestPrime = 0


def find_largest_prime_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num /= i
    return num


print find_largest_prime_factor(number)
