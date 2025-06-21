n = int(input())
s = input()

c_curr = ""
ans = 0
for c in s:
    if c != c_curr:
        ans += 1
        c_curr = c
print(ans)
