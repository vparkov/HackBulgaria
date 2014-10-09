import math	

def if_prime(n):
	count = 0
	for i in range(1, n + 1):
		if n % i == 0:
			count += 1
	if count == 2:
		return True

	return False


def prime_num_divs(n):
	result = 0
	count = 0

	while n > 0:
		for i in range(1, n + 1):
			if n % i == 0:
				count += 1

		n //= 10

	if if_prime(count) == True:
		return True
		
	return False


def main():
	n = input("Give me number!!\n")
	print(prime_num_divs(int(n)))


if __name__ == '__main__':
	main()