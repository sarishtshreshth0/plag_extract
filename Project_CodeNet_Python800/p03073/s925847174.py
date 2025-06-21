s = str(input())
n = len(s)
a = 0
b = 0
apple = ("10" * n)[:n]
orange = ("01" * n)[:n]
for i in range(n):
    if apple[i] != s[i]:
        a += 1
    if orange[i] != s[i]:
        b += 1
print(min(a, b))