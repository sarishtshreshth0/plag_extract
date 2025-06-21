n = input()
s = input()

slime = s[0]
for index in range(1,len(s)):
  if s[index] != s[index-1]:
    slime += s[index]
print(len(slime))