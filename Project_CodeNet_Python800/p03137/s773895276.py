N,M = map(int,input().split())
X = sorted(list(map(int,input().split())))
D = sorted([X[n+1]-X[n] for n in range(M-1)])

if M<=N:
  print(0)
else:
  print(sum(D[:M-N]))