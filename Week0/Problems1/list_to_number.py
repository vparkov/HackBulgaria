def is_number_balanced(n):
	if n // 10 == 0:
		return True

	temp = n
	length = 0
	while temp > 0:
		length += 1
		temp //= 10

	rightPart = 0
	halflen = length // 2
	while halflen > 0:
		rightPart += n % 10
		n //= 10
		halflen -= 1

	if length % 2 != 0:
		n //= 10

	leftPart = 0
	while n > 0:
		leftPart += n % 10
		n //= 10

	if leftPart == rightPart:
		return True
	return False

print(is_number_balanced(1238033))