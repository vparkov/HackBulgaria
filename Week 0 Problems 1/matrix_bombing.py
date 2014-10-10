def matrix_bombing_plan(m, input):
	x = input[0]
	y = input[1]
	for i in range(x - 1, x + 1):
		for j in range(y - 1, y + 1):
			m[i][j] = 1
			#if(i != x and j != y):
				#print(m[i][j] - m[x][y])
				#if(m[i][j] - m[x][y] >= 0):
					#m[i][j] -= m[x][y]
							
	print(m)


#input = [2, 2]
#m = [[1, 1, 4], [1, 3, 5], [1, 6, 1]]
#print(m)
print(matrix_bombing_plan([[5, 1, 4], [1, 3, 5], [1, 6, 1]], [1, 1]))