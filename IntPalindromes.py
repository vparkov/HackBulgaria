def is_int_palindrome(n):
	r = str(n)
	return r == r[::-1]


print(is_int_palindrome(3334))