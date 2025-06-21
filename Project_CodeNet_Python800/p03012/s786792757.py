N = int(input())
W = list(map(int,input().split()))
W.insert(N,0)
left,right = 0,0
S = 1000
for i in range(0,N):
	left += W[i]
	right = sum(W) - left
	S =min(S,abs(left - right))
print(S)