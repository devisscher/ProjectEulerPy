
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(x):
	return str(x) == str(x)[::-1]

def fn(n):
	maxPalindrome = 1
	for x in range(n, 1, -1):
		for y in range(n,x-1,-1):
			if isPalindrome(x*y) and x*y > maxPalindrome:
				maxPalindrome = x*y
			elif x * y < maxPalindrome:
				break
	return maxPalindrome

print(fn(999))