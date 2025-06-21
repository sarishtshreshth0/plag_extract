n = int(raw_input())

def dfs(u, n,c):
	if u > n:
		return
	if u != 0: 
		if set(str(u)) == set(['3','5','7']):
			c[0] += 1
	
	for digit in [3,5,7]: dfs(u*10 + digit,n,c)

c = [0]
dfs(0, n, c)
print c[0]