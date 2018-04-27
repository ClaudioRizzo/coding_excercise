'''
Given an array of integer, find the longest subsequence: return how long it is.
To begin with, assume that the integers are all positives and that the array is not ordered.
Also, assume no duplicates are in the array
'''

def longestSequence(numbers):
	
	if len(numbers) <= 1: return len(numbers)

	support = {}
	for i in range(len(numbers)):
		support[numbers[i]] = i

	m = 0
	for n in numbers:
		if n in support:
			c = 1 # this is the current length
			left = n-1
			right = n+1

			while left in support or right in support:
				if left in support:
					c += 1
					del support[left]
					left -= 1
				if right in support:
					c += 1
					del support[right]
					right += 1

			m = max(m, c)

	return m


	



def main():
	a = [1,0,3,2,5,7,6,9,8,10]
	
	print( longestSequence(a) )

if __name__ == '__main__':
	main()