s = list(map(int,input()))

n = int(len(s)/2)

a = [0]*len(s)
b = [0]*len(s)

for i in range(n):
  a[2*i] = 0
  a[2*i+1] = 1
  b[2*i] = 1
  b[2*i+1] = 0

if len(s)%2 ==1:
  a[len(s)-1] = 0
  b[len(s)-1] = 1 


an = 0
bn = 0

for j in range(len(s)):
  if a[j] != s[j]:
    an += 1
  if b[j] != s[j]:
    bn += 1

print(min(an, bn))
