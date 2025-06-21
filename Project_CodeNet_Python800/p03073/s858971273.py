s = input()
a = ''
b = ''
for i in range(len(s)):
  if i % 2 == 0:
    a += '0'
    b += '1'
  else:
    a += '1'
    b += '0'
c = 0
for x, y in zip(s, a):
  if x != y:
    c += 1
d = 0
for x, y in zip(s, b):
  if x != y:
    d += 1
print(min(c, d))