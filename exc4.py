# # Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

_range = range(999, 100, -1)
largestPalindrome = 0


def reverse(num):
    reversednum = 0
    while num:
        reversednum = reversednum * 10
        reversednum = reversednum + num % 10
        num = num / 10
    return reversednum


def is_palindrome(num):
    return num == reverse(num)


for i in _range:
    for j in _range:
        checkPalindrome = i*j
        if is_palindrome(checkPalindrome):
            if checkPalindrome > largestPalindrome:
                largestPalindrome = checkPalindrome

print("Largest palindrome: " + str(largestPalindrome))


