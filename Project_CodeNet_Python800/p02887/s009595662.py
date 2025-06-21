N = int(input())
S = input()
ans = 0
prev = -1
for s in S:
  if prev != s:
    ans+=1
    prev=s
print(ans)