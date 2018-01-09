'''
Given an array S (may have negative numbers) and an Integer i (May be negative),
find the smallest subarray S' such that sum(S') >= i
'''

# Easy solution
# 1. find all the sub array
# 2. for each subarray extract the ones that sum(s') >= i
# 3. of the subarrays at 3, extract the smalelst(s) (with less elements)

# This solution can takes O(n^2) as there are n*(n+1) / 2 ~ n^2 total sub-arrays

# A better solution
# construct the max subarray. The first max subarray we find wich respect the propery of sum(S) >= i is also our solution
# this is true because we divide the problem in smaller sub-problems (so until array long 1). for each of this we find a with
# iteration the max sub array at a given index and we check agains i. If it is greater, than we have our solution if not we go
# on.

# a -> is the array we want to analyze
# k -> integer we want to check the sum against
def sub_array_integer(a, k):
	max_sub = a[0]
	min_length = 1

	for i in range(1, len(a)):
		if max_sub >= i:
			

		if a[i] > a[i] + max_sub:
			s=i
			max_sub = a[i]
		else:
			max_sub += a[i]
		
		if max_global < max_sub:
			e = i
			max_global = max_sub



def main():


if __name__ == '__main__':
	main()

