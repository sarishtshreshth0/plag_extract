n = int(input())
s = input()
ans = 0
pc = ''
for i in s:
    if i != pc:
        ans += 1
    pc = i
print(ans)