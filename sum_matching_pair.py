def find_sum(a, k):
    # a is sorted for us
	i = 0
	j = len(a) - 1	
	while i < j:
		c_sum = a[i] + a[j]
		if c_sum > k:
			j -= 1
		elif c_sum < k:
			i += 1
		else:
			return (i,j)
	return None

def find_sum_general(a, k):
	diffs = set()
	
	for num in a:
		diffs.add(k-num)
	
	for num in a:
		if num in diffs:
			return True
	
	return False



if __name__ == '__main__':
    print(find_sum_general([1,2,4,4], 8))