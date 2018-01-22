
def lastDup(a):
	tmp = None
	for i in range(len(a) -1, 0, -1):
		if a[i] == tmp:
			return i+1
		else:
			tmp = a[i]
	return False
def main():
	print( lastDup([1,2,5,6,6,7,9]) )

if __name__ == '__main__':
	main()