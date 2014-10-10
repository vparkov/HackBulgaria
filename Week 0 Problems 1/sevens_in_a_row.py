import math	

def sevens_in_a_row(arr, n):
	count = 0
	for i in range(0,6):
		if arr[i] == 7:
			count += 1
	
	if count == n:
		return True

	return False



print(sevens_in_a_row([10, 8, 7, 7, 7, 4], 3))