
def brute_max(a):
	
	old_sum = -1
	max_i = -1
	max_j = -1
	for i in range(len(a)):
		current_sum = 0
		for j in range(i, len(a)):
			current_sum += a[j]
			if old_sum < current_sum:
				old_sum = current_sum
				max_i = i
				max_j = j
		
	return (old_sum, max_i, max_j)

def eff_max(a):
	max_global = a[0]
	max_sub = a[0]
	s = 0
	e = 0
	for i in range(1, len(a)):
		if a[i] > a[i] + max_sub:
			s=i
			max_sub = a[i]
		else:
			max_sub += a[i]
		if max_global < max_sub:
			e = i
			max_global = max_sub

	return (max_global, s, e)



def main():
	a = [1,2,3,-100]
	print( eff_max(a) )

if __name__ == '__main__':
	main()