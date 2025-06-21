n = int(input())
w = list(map(int, input().split()))
l = []
for t in range(n-1):
  l.append(abs(sum(w[0:t+1])-sum(w[t+1:n])))
print(min(l))