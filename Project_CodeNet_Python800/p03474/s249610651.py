a, b = map(int, input().split())
s = input()

if s[a] != '-':
  ans = 'No'
else:
  cnt = s.count('-')
  if cnt > 1:
    ans = 'No'
  else:
    ans = 'Yes'
    
print(ans)