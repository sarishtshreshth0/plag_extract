a, b = map(int, input().split())
S = input()

for i in range(len(S)):
  if (i == a and S[i] != "-") or (i != a and S[i] =="-"):
    print("No")
    exit()
print("Yes")