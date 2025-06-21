n = int(input())
s = list(input())
ans = ''
cnt = 0
for c in s:
    ans += c
    if c == ')':
        cnt -= 1
    else:
        cnt += 1
    if cnt < 0:
        ans = '(' + ans
        cnt = 0

cnt = 0
for c in s[::-1]:
    if c == ')':
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        ans += ')'
        cnt = 0

print(ans)