n = int(input())
s = input()
i = 0
while i < len(s)-1:
    if s[i] == s[i+1]:
        s = s[:i] + s[i+1:]
        i -= 1
    i += 1
print(len(s))
