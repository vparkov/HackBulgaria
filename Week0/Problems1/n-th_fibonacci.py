def nth_fibonacci(n):
	if n == 1 or n == 2:
		return 1

	else:
		return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

def main():
	n = input("Give me number!!\n")
	print(nth_fibonacci(int(n)))

if __name__ == '__main__':
	main()