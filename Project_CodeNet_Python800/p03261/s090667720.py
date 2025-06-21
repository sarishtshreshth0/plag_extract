N = int(input())
strl = [input()]
for i in range(N-1):
  s = input()
  if s in strl or s[0] != strl[i][-1]:
    print("No")
    exit()
  else:
    strl.append(s)
print("Yes")
