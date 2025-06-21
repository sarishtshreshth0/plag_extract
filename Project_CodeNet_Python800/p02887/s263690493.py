n = int(input())
s = list(input())
b = 0
d = s[0]
for i in range(n):
    if d != s[i]:
        d = s[i]
        b += 1

print(b+1)
