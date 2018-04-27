'''
Given an arrays of "towers", implement the function is hoppable which returns true if it
is possible to escape the array by jumping tower to tower.

Each cell of the array contains a value which is the hight of the tower. One can jump forward
of as many cells as the hight of the tower she started from.
For example given the array [4,2,0,0,2,0], from each index here is where one can jump:

0 -> {1, 2, 3, 4}
1 -> {2, 3}
2 -> {None}
3 -> {None}
4 -> {5, Out}
5 -> {None}
'''

def best_move(towers, index):
	
	_max = towers[index]
	m_index = index

	for i in range(towers[index]):
		k = index + i + 1
		if k > len(towers) - 1:
			return k 
		if _max < towers[k] + index+k:
			_max = towers[k] + index+k
			
			m_index = k
	return m_index
		


def is_hoppable(towers):
	index = 0
	while True:
		i = best_move(towers, index)

		if(i == index): return False
		index = i
		if index > len(towers) - 1:
			return True
	
	# return hoppable(towers,0, dict({}))

def hoppable(towers, index, memo):
	
	if index in memo: return memo[index]
	
	if index > len(towers)-1:
		# we are done with this branch
		memo[index] = False
		return False

	if towers[index] > len(towers) - index - 1:
		# We can escape!!!
		memo[index] = True
		return True
		
	
	for i in range(1, towers[index]+1):
		k = i+index
		out = hoppable(towers, k, memo)
		memo[k] = out
		if out: return True
	
	memo[index] = False
	return False

		 
def main():
	#print(best_move([4,5,0,0,1,0], 0))
	print( is_hoppable([4,5,0,0,1,0]	) )


if __name__ == '__main__':
	main()