n = int(input())
s = str(input())
s += "A"
q = s[0]
ans = 0
for i in range(n+1):
  if(q==s[i]):
    None
  else:
    ans += 1
    q = s[i]
print(ans)
