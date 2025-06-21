n = int(input())
s = input()
ans = n

if n == 1:
  print("1")
else:
  for i in range(n-1):
    if s[i] == s[i+1]:
      ans -= 1
  print(ans)