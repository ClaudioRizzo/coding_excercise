'''
Steve has a string, s, consisting of  lowercase English alphabetic letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after operation.

Steve wants to reduce  as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing 's non-reducible form!

Note: If the final string is empty, print Empty String .

Input Format

A single string, s.

Constraints

1 <= n <=100

Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.
'''

# a: original array
# l: index to left beginning
# m: index to middle of array
# r: index to end of rigth array
def merge(a, l, m, r):
	#n1 = m - l + 1 # left length
	#n2 = r - m # rigth lentgth

	#L = [ a[i] for i in range(n1-1) ]
	#R = [ a[j] for j in range(n1-1, n1+n2-1) ]
	#print("l: %d" % l)
	#print("m: %d" % m)
	#print("r: %d" % r)
	if a[m-1] == a[m] and a[m-1] != '$' and a[m] != '$':
		a[m-1] = ''
		a[m] = ''
	

def super_reduce(s, l, r):
	if l < r:
		m = int((l + r) / 2)
		super_reduce(s, l, m)
		super_reduce(s, m+1, r)
		merge(s, l, m, r)
		print(s)	
	return s		
		


def main():
	print('enter string to reduce')
	s = input('> ')

	result = super_reduce(list(s), 0, len(s))
	
	result = list(filter(lambda x: x != '', result))
	
	if result:
		result = ''.join(result)
	else:
		result = "Empty String"
	
	print(result)

if __name__ == '__main__':
	main()