# n is the Sum + 1 and m is the coins.length() + 1
def coin_change(dp, coins m, n):
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			if coins[j - 1] >=
	return dp[m][n]
	
input = raw_input().strip()
S, m = input.split(' ')
S, m = [int(S), int(m)]

#Initialize the dp
dp = []
for i in range(m + 1):
	dp.append([])
	
for i in range(m + 1):
	dp[i].append(1)
	
for i in range(1, S + 1):
	dp[0].append(0)