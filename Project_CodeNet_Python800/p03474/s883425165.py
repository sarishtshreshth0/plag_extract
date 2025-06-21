import sys

a, b = map(int, input().split())
s = input()

for i in range(a + b + 1):
  if i < a and s[i] == '-':
    print('No')
    sys.exit()
  elif i == a and s[i] != '-':
    print('No')
    sys.exit()
  elif i > a + 1 and s[i] == '-':
    print('No')
    sys.exit()
print('Yes')