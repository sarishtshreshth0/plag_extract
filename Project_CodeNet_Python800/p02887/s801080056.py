N = int(input())
s = input()
cnt = 1
i = 1
while (i < N):
    if s[i] != s[i-1]:
        cnt += 1
    i += 1
print(cnt)