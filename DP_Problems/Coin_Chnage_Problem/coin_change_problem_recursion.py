def coin_change(S, coins, m):
	if S < 0:
		return 0
		
	if S == 0:
		return 1
	
	if m == 0 and S > 0:
		return 0
		
	return coin_change(S, coins, m - 1) + coin_change(S - coins[m - 1], coins, m)
	
input = raw_input().strip()
S, m = input.split(' ')
S, m = [int(S), int(m)]

coins = map(int, raw_input().strip().split(' '))
print coin_change(S, coins, m)