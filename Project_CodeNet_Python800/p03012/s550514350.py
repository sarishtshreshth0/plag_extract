N = int(input())
W = list(map(int, input().split()))
a = 0
b = sum(W)
dif = b

for i in range(N):
  a += W[i]
  b -= W[i]
  if dif > abs(b-a):
    dif = abs(b-a)
  else:
    break
    
print(dif)