import math	

def sevens_in_a_row(arr, n):
	count = 0
	for i in range(0, len(arr)):
		if arr[i] == 7:
			count += 1
	
	if count == n:
		return True

	return False



print(sevens_in_a_row([1, 7, 1, 7, 7], 4))