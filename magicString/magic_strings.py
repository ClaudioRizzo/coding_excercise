'''
Magical binary strings are non-empty binary strings if the following two conditions are true: 
 1. The number of 0's is equal to the number of 1's.
 2. For every prefix of the binary string, the number of 1's should not be less than the number of 0's.

A magical string can contain multiple magical substrings. If two consecutive substrings are magical, 
then we can swap the substrings as long as the resulting string is still a magical string. 
Given a magical binary string, str, perform zero or more swap operations on its consecutive magical substrings 
such that the resulting string is as lexicographically large as possible. 
Two substrings are considered to be consecutive if the last character of the 
first substring occurs exactly one index before the first character of the second substring.
'''

def same_zero_one(s):
	zero = 0
	one = 0
	for c in s:
		if c != '0' and c != '1':
			return False
		elif c == '0':
			zero += 1
		else: 
			one += 1

	return zero == one


def __generate_prefix(s, prefixes, i):
	if i == len(s)+1:
		return prefixes
	else:
		prefixes.append(s[0:i])
		i+=1
		return __generate_prefix(s, prefixes, i)

def generate_prefix(s):
	return __generate_prefix(s,[], 1)


def get_sublen(s, subs, i, count):
	if s == "":
		return subs
	else:
		start = count
		end = count + i - 1
		if len(s[0:i]) == i: subs.append((s[0:i], start, end))
		count += 1
		return get_sublen(s[1:], subs, i, count)

def get_substrings(s):
	subs = []
	for i in range(1, len(s)+1):
		subs += get_sublen(s, [], i, 0)

	return subs
	

def more_one(s):
	return s.count('0') <= s.count('1')

def is_magical(s):
	if same_zero_one(s):
		for p in generate_prefix(s):
			if not more_one(p):
				return False
		return True
	else:
		return False

def main():
	print(get_substrings("abcde"))

if __name__ == '__main__':
	main()