n = int(input())
a = list(map(int, input().split()))

count = [0]*(max(a)+1)
for i in a: count[i]+=1

if len(count) <= 2:
  print(sum(count))
  exit()
  
ans = 0
for i in range(2,max(a)):
  if count[i-1]+count[i]+count[i+1] > ans:
    ans = count[i-1]+count[i]+count[i+1]
print(ans)