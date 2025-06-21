s = input()
n = len(s)
cn0 = 0
cn1 = 0
for i in range(n):
    if s[i] != str(i % 2):
        cn0 += 1
for i in range(n):
    if s[i] != str((i+1)%2):
        cn1 += 1
print(min(cn0, cn1))