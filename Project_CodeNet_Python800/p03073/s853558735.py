s = input()
n = len(s)
x1, x2 = 0, 0
for i in range(n):
    if s[i] != str(i%2):
        x1 += 1
    if s[i] != str((i+1)%2):
        x2 += 1
print(min(x1, x2))