a,b = map(int,input().split())
ck = 0
for c in range(1,4):
  if a*b*c % 2:
    ck = 1
    break
print('Yes' if ck else 'No')