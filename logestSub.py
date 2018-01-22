
def longest(s):
	m = 0
	tmp = 0
	index = 0
	tmp_index = 0

	for i in range(len(s)):
		if i == 0:
			m = 1
			tmp = 1
		elif s[i] == s[i-1]:
			tmp+=1
			tmp_index = i
		else:
			m = max(tmp, m)
			if m == tmp: index = tmp_index
			tmp = 1

	return {s[index]: m}

def main():
	print( longest("") )
 
if __name__ == '__main__':
	main()