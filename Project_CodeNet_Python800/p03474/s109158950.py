a, b = map(int, input().split())
s = input()
if s[:a].isdigit() and s[a] =='-' and s[-b:].isdigit():
  print('Yes')
else:
  print('No')
