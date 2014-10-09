def sum_of_digits(n):
	result = 0

	while n > 0:
		result += n % 10
		n //= 10

	return result

def main():
	n = input("Give me number!!\n")
	print(sum_of_digits(int(n)))

if __name__ == '__main__':
	main()