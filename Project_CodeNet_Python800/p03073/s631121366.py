S = input()
s = []
for _ in S:
  s.append(int(_))
s1 = [1]
s2 = [0]
for i in range(1,len(s)):
  if s1[i-1] == 0:
    s1.append(1)
  else:
    s1.append(0)
  if s2[i-1] == 0:
    s2.append(1)
  else:
    s2.append(0)
    
a = 0
b = 0
for j in range(len(s)):
  if s[j] != s1[j]:
    a += 1
  if s[j] != s2[j]:
    b += 1
print(min(a,b))