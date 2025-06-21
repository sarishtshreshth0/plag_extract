n,k = map(int,input().split())

i = 0
while True :
  s = k **i
  if n < s :
    ans = i
    break
  i += 1
  
print(ans)