n,k =map(int,input().split())
digitlist = []

while (n/k != 0):
	tmp = n%k
	digitlist.insert(0,(tmp))
	n = n//k

print(len(digitlist))