S = input()
L = len(S)
c = 0
j = 0
for i in range(L):
  c += abs(j-int(S[i]))
  j ^= 1
print(min(c, L-c))