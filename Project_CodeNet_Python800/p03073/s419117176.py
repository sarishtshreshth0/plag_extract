s = list(input())
cnt = 0
if s[0] == "0":
    for i in range(len(s)):
        if s[i] != str(i % 2):
            cnt += 1
else:
    for i in range(1, len(s) + 1):
        if s[i - 1] != str(i % 2):
            cnt += 1
print(cnt)
