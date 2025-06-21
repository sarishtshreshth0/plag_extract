n = int(input())
a = list(map(int, input().split()))

list = [0]*100000
for i in range(n):
  list[a[i]] += 1

ans = 0
for i in range(1,99999):
  sum = list[i-1]+list[i]+list[i+1]
  ans = max(sum, ans)
  
print(ans)