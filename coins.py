memory = dict()

def f(coins, tg):
	if tg == 0:
		return 1
	elif tg < 0: 
		return 0

	if (coins[0], tg) in memory:
		return memory[(coins[0], tg)]

	result = 0
	for i in range(len(coins)):
		c = coins[i]	
		r = f(coins[i:], tg-c)
		memory[(coins[0], tg-c)] = r
		result += r

	return result

def main():
	print(f([2,5,3, 6], 10))
	print(memory)
if __name__ == '__main__':
	main()