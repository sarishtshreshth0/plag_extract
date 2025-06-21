n = int(input())
s = set()
w = input()
last = w[-1]
s.add(w)
for i in range(n - 1):
  w = input()
  if w in s or w[0] != last:
    print('No')
    exit()
  else:
    last = w[-1]
    s.add(w)
print('Yes')