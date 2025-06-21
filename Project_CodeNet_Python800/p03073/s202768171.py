s = list(map(int, list(input())))

for i in range(len(s)):
    if i % 2 == 0:
        s[i] = bool(s[i])
    else:
        s[i] = not s[i]

print(min(sum(s), len(s) - sum(s)))