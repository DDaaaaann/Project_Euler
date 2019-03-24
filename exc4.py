# # Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

range = range(999, 100, -1)
largestPalindrome = 0

def reverse(num):
    reversednum = 0
    while num:
        reversednum = reversednum * 10
        reversednum = reversednum + num % 10
        num = num / 10
    return reversednum


def ispalindrome(num):
    return num == reverse(num)


for i in range:
    for j in range:
        checkPalindrome = i*j
        if ispalindrome(checkPalindrome):
            if checkPalindrome > largestPalindrome:
                largestPalindrome = checkPalindrome

print("Largest palindrome: " + str(largestPalindrome))


