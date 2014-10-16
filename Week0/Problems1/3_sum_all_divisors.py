import math	

def sum_of_divisors(n):
	result = n

	for i in range(1, n):
		if n % i == 0:
			result += i
			
	return result

def main():
	n = input("Give me number!!\n")
	print(sum_of_divisors(int(n)))


if __name__ == '__main__':
	main()