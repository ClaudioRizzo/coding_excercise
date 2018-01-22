import time
from random import shuffle

def main(numbers):
	index_table = {}

	# init support hash table in O(n)
	for i in range(len(numbers)):
		index_table[numbers[i]] = i

	_min = None
	_max = None

	# I use an hash table as support initialized with all the numebers in the array
	# max and min are respectively the number on the right (so growing) 
	# and on the left (so decreasing)

	for n in numbers:
		if n in index_table:
			g = {n: index_table[n]}
			del index_table[n]
			_min = n-1
			_max = n+1
			while _min in index_table or _max in index_table:
				if _min in index_table:
					g[_min] = index_table[_min]
					del index_table[_min]
					_min -= 1
				if _max in index_table:
					g[_max] = index_table[_max]
					del index_table[_max]
					_max += 1
					
			a = [None for _ in range(len(numbers))]

			for k in g:
				a[g[k]] = k

			res = [x for x in a	if x != None]
			#print(res)

			




			
			 

if __name__ == '__main__':
	l = []
	for i in [2**i for i in range(32)]:
		l = [x for x in range(i*10000)]
		

		start = time.time()
		main(l)
		end = time.time()
		print( (end - start) )