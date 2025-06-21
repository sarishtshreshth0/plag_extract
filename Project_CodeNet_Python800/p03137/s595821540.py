N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))
G = [abs(X[i+1]-X[i]) for i in range(M-1)]
G.sort(reverse=True)
print(sum(G[N-1:]))