n = int(input())
w = list(map(int,input().split()))
l = []
for i in range(n-1):
  a = abs(sum(w[0:i+1]) - sum(w[i+1:n+1]))
  l.append(a)
print(min(l))
