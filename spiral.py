


def spiral(m):
	N = len(m) * len(m[0])

	j_max = len(m[0]) - 1
	j_min = 0
	increment_j = True

	i_min = 0
	i_max = len(m)-1
	increment_i = True
	
	counter = 0
	even = 1
	while counter < N:
		if even%2:
			if increment_j:
				for j in range(j_min, j_max+1):
					print(m[i_min][j])
					counter += 1
				i_min += 1
				increment_j = False
			else:
				for j in range(j_max, j_min-1, -1):
					print(m[i_max][j])
					counter += 1
				i_max -= 1
				increment_j = True
		else:
			if increment_i:
				for i in range(i_min, i_max+1):
					print(m[i][j_max])
					counter += 1
				j_max -= 1
				increment_i = False
			else:
				for i in range(i_max, i_min-1, -1):
					print(m[i][j_min])
					counter += 1
				j_min += 1
				increment_i = True

		even += 1



def main():
	m = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
	spiral(m)

if __name__ == '__main__':
	main()