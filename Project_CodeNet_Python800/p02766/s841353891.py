N,K = map(int,input().split())

D = 0

while N > 0:
  N //= K
  D += 1
  
print(D)