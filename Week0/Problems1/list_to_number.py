def list_to_number(digits):
	num = int(''.join(map(str,digits)))
	return num


print(list_to_number([1,2,3]))