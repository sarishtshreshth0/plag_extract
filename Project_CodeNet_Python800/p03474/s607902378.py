A,B = map(int,input().split())
S = input()
ans = "Yes"
for i in range(len(S)):
  if i == A:
    if S[i] != "-":
      ans = "No"
  else:
    if S[i] == "-":
      ans = "No"
print(ans)