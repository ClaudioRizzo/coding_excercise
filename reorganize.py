'''
Given a string, 
check if it is can be reorganized such that the same char is not next to each other, 
If possible, output a possible result:
input: google
output: gogole
'''

def check_condition(letters, n):
	m = 0
	k_max = ""
	for k in letters:
		if m<letters[k]:
			m = letters[k]
			k_max = k

	if m > n-m+1: return (False, m, k_max)
	else: return (True, m, k_max)

def flat_map(letters, c):
	s = ""
	for k in letters:
		if k != c:
			s+=k*letters[k]
	return s

def main():
	s = "CCBAA"

	letters = {}

	for c in s:
		if c not in letters:
			letters[c] = 1
		else:
			letters[c] += 1


	feasible, m, k = check_condition(letters, len(s))

	if feasible:
		lists = []
		for i in range(m):
			lists.append([k])
	
		flat = flat_map(letters, k)
		
		i = 0
		while i < len(flat):
			for l in lists:
				if i < len(flat):
					l.append(flat[i])
					i+=1
		result = []
		for l in lists:
			result+=l
		print(result)
	else:
		print("FOTTITI")

if __name__ == '__main__':
	main()