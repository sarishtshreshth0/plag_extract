s = input()
 
start0 = 0
start1 = 0
for i in range(len(s)):
  if i % 2 == 0:
    if s[i] == "0":
      start1 += 1
    elif s[i] == "1":
      start0 += 1
  elif i % 2 == 1:
    if s[i] == "0":
      start0 += 1
    elif s[i] == "1":
      start1 += 1

print(min([start0, start1]))