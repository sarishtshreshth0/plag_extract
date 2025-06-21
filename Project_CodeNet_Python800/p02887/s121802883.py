n = int(input())
s = str(input())

new_s = s[0]

for i in range(1,len(s)):
    if s[i] == s[i-1]:
        continue
    else:
        new_s += s[i]

print(len(new_s))
