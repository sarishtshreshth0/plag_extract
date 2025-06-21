n = int(input())
s = input()

ans = 0
prev = ''
for si in s:
    if prev == si:
        continue
    else:
        ans += 1
        prev = si

print(ans)