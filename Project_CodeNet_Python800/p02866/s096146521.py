N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
	print(0)
	exit()

D = sorted(D)
V = [0]*(D[-1]+1)

for i in range (0, N):
	V[D[i]]+=1

if V[0] > 1:
	print(0)
	exit()
else:
	count = 1

for i in range (0, len(V)-1):
	if V[i] == 0 and V[i+1] > 0:
		print(0)
		exit()
	else:
		count*= V[i]**V[i+1]
        
print(count%998244353)