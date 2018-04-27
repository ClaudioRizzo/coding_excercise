def move(a, x):
	if x > len(a)-1 or x < 0:
		return -1
	else:
		return a[x]

def cycles(a):
	fast = 0
	slow = 0

	while True:
		fast = move(a, fast)
		fast = move(a, fast)
		slow = move(a, slow)

		if fast < 0 or slow < 0:
			return False
		if fast == slow:
			return True


def main():
	print( cycles([1,2,3,1,8]) )

if __name__ == '__main__':
	main()