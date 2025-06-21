N, K = map(int, input().split())
count = 1

while N >= K:
  N //= K
  count +=1
  
print(count)