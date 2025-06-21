n = int(input())
dv = 0
for s in str(n):
  dv += int(s)
print('Yes' if n % dv == 0 else 'No')