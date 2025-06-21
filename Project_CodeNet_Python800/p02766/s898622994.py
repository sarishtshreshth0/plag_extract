N, K = map(int, input().split())
n=0
while True:
  N//=K
  if not N:
    break
  n+=1
print(n+1)