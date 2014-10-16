import math	

def if_prime(n):
	count = 0
	for i in range(1, n + 1):
		if n % i == 0:
			count += 1
	if count == 2:
		return True

	return False


def main():
	n = input("Give me number!!\n")
	print(if_prime(int(n)))


if __name__ == '__main__':
	main()