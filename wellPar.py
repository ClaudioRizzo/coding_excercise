def isWellPar(s):
	stack = []

	for c in s:
		if c == '(':
			stack.append(')') 
		elif c == '[':
			stack.append(']') 
		elif c == '{':
			stack.append('}')
		elif c == ')' or c == ']' or c == '}':
			
			if c != stack.pop():
				return False
	
	return not stack
	


def main():
	print( isWellPar("abcdefghi()[abcdef]\{\}"))

if __name__ == '__main__':
	main()