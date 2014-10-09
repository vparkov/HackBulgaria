def contains_Digits(number, digits):
	count = 0
	while number > 0:
		for i in range(0, len(digits)):
			if number % 10 == digits[i]:
				count += 1
		number //= 10
	if count == len(digits):
		return True
	return False

print(contains_Digits(134567, [4, 2, 3]))