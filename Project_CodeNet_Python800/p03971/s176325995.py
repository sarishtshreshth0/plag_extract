N, A, B = map(int, input().split())
S = input()
a = 0
b = 0
for i in range(N):
  if S[i] == "a" and a + b < A + B:
    print("Yes")
    a += 1
  elif S[i] == "b" and a + b < A + B and b < B:
    print("Yes")
    b += 1
  else:
    print("No")