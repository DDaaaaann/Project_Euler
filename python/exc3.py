# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

number = 1000
currentPrime = 2


def findlargestprimefactor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            print i
            num /= i
    print num


findlargestprimefactor(number)
