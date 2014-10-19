def is_decreasing(seq):
	count = 0
	for i in range(0, len(seq) - 1):
		if seq[i] > seq[i + 1]:
			count += 1
	if count == len(seq) - 1:
		return True
	return False


print(is_decreasing([1,1,1]))