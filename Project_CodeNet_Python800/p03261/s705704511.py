N = int(input())
A = [input() for _ in range(N)]
if len(set(A)) != N:
  print("No")
  exit()
for i, a in enumerate(A):
  if i == 0:
    continue
  if a[0] != A[i-1][-1]:
    print("No")
    exit()
print("Yes")