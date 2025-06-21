def tenToK(N, K):
	if N // K:
		return tenToK(N // K, K) + str(N % K)
	else:
		return str(N % K)

N, K = map(int, input().split())
print(len(tenToK(N, K)))
