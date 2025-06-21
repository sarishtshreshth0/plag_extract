s = input()
w = 0
n = int(s)

for i in range(len(s)):
  w += int(s[i])
print("Yes" if n%w == 0 else "No")