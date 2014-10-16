def number_to_list(n):
	b = str(n)
	c = []

	for digit in b:
		c.append(int(digit))
	return c

print(number_to_list(32322323))