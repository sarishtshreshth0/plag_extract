a,b = map(int,input().split())
s = list(input())
n = len(s)
ans = "No"
for i in range(n):
  if s[i] == "-":
    if a == i:
      ans = "Yes"
if s.count("-") > 1:
  ans = "No"
      
print(ans)

