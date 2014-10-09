import math	

def sum_of_divisors(n):
	result = 0
#	temp = n

	while n > 0:
		for i in range(1, n + 1):
			if n % i == 0:
				result += i

		n //= 10

	return result

def main():
	n = input("Give me number!!\n")
	print(sum_of_divisors(int(n)))


if __name__ == '__main__':
	main()