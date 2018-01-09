import time


def add_elem(s, e):
	a = list(s)
	a.append(e)
	return a

def subsets(_set):
	subsets = list([[]])
	generated = []
	for e in _set:
		for s in subsets:
			k = list(s)
			k.append(e)
			generated.append(k)
		subsets+=generated
		generated = []
	return subsets






		





def main():
	print(subsets([1,2,3]))

if __name__ == '__main__':
	main()