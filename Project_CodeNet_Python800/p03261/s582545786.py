n = int(input())
w = [input() for _ in range(n)]
ans = 'Yes'
if len(set(w)) != len(w):
  ans = 'No'
for i in range(n-1):
  if w[i][-1] != w[i+1][0]:
    ans = 'No'
    break
print(ans)