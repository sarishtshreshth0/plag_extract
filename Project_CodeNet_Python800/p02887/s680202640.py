n = int(input())
s = input()

ans = 0
before = ""
for i in s:
    if i != before:
        ans += 1
        before = i

print(ans)