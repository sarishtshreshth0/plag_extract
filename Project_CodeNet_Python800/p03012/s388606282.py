n = int(input())
lisw = list(map(int,input().split()))

total = 100000000
for i in range(1,n):
  total = min(total,abs(sum(lisw[:i])-sum(lisw[i:])))
  
print(total)