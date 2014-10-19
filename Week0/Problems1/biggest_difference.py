def biggest_difference(arr):
	min = 0
	for i in range(1,len(arr) - 1):
		for j in range(2,len(arr)):
			if arr[i] - arr[j] < min:
				min = arr[i] - arr[j]
			print(min, "one")
			if arr[j] - arr[i] < min:
				min = arr[j] - arr[i]
			print(min, "two")
	return min


print(biggest_difference([1,2,3,4,5]))