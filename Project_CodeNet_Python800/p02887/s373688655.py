input()
cnt = 0
x = ""
for s in input():
    if x != s:
        cnt += 1
        x = s
print(cnt)