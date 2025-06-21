s = input()
pattern1 = 0
pattern2 = 0
for i in range(len(s)):
  if i %2 == 0:
    if s[i] == "0":
      pattern1 += 1
    else:
      pattern2 += 1
  else:
    if s[i] == "0":
      pattern2 += 1
    else:
      pattern1 += 1
print(min(pattern1,pattern2))