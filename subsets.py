import time




def add_elem(s, e):
	a = list(s)
	a.append(e)
	return a

def subsets(_set):
	
	subsets = list([[]])
	generated = []
	for e in _set:
		i=0
		for s in subsets:
			k = list(s)
			k.append(e)
			generated.append(k)
			i+=1
		subsets+=generated
		generated = []
		print(i)
	return subsets



def main():
	print(subsets([1,2,3,4,5,6,7]))

if __name__ == '__main__':

	main()