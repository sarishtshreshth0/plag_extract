S = list(input())

pattern1, pattern2 = [], []
for i in range(len(S)):
  if i % 2 == 0:
    pattern1.append('0')
    pattern2.append('1')
  else:
    pattern1.append('1')
    pattern2.append('0')

ham1, ham2 = 0, 0
for i in range(len(S)):
  if pattern1[i] != S[i]:
    ham1 += 1
  if pattern2[i] != S[i]:
    ham2 += 1
print(min(ham1, ham2))