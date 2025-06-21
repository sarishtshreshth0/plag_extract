n = int(input())
s = input()

cnt = 1
for r in range(1, n, 1):
    if s[r] != s[r-1]:
        cnt += 1

print(cnt)