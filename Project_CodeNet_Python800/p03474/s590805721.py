A, B = map(int, input().split())
S = input()
X = {str(i) for i in range(0, 10)}
f = 0
for i in range(A+B+1):
  if i != A and S[i] not in X:
    f = 1
    break
  if i == A and S[i] != "-":
    f = 1
    break
if f == 0:
  print("Yes")
else:
  print("No")