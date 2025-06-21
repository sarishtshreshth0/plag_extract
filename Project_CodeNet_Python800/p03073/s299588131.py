s = input()
count = 0
tmp = s[0]
for i in range(1, len(s)):
    if s[i] == tmp:
        count += 1
        if s[i] == "0":
            tmp = "1"
        else:
            tmp = "0"
    else:
        tmp = s[i]

print(count)