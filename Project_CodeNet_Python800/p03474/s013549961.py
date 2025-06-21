a,b = map(int, input().split())
s = input()
if b == 1:
  print("Yes" if s[0:a].isdecimal() and s[a] == "-" and s[-1].isdecimal() else "No")
else:
  print("Yes" if s[0:a].isdecimal() and s[a] == "-" and s[a+1:].isdecimal() and s[-b-1] == "-" else "No")