'''
Given an ordered array, find element k in it
'''

def find_k(a, l, r, k):
	middle = (l+r) // 2

	if l>r:
		return -1
	elif k < a[middle]:
		return find_k(a, l, middle, k)
	elif k > a[middle]:
		return find_k(a, middle, r, k)
	else:
		return middle


def main():
	a = [1,2,2,3,4,5,6,7,8,9,10,30,50,80,90]
	print( find_k(a, 0, len(a), 1) )

if __name__ == '__main__':
	main()