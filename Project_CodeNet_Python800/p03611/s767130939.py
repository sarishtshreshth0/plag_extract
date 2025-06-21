n = int(input())
a = list(map(int,input().split()))
lst = [0]+[0]*(10**5 + 1)
for i in a:
  lst[i] += 1
  
ans = 0
for i in range(1,10**5):
  ans = max(ans,lst[i-1]+lst[i]+lst[i+1])
print(ans)