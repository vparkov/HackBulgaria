def sum_matrix(m):
	return sum(sum(x) for x in m)

print(sum_matrix([[1, 1, 1], [6, 4, 3], [2, 3, 6]]))