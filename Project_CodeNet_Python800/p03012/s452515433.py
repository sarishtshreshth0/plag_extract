n = int(input())
w = list(map(int,input().split()))
a = []
for i in range(n):
  b = sum(w[:i+1])
  b_s = sum(w[i+1:])
  a.append(abs(b - b_s))
  
print(min(a))