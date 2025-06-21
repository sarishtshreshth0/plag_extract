n = input()
n = input()
cnt = 0
a = n[0]
for i in range(1,len(n)):
    if a == n[i]:
        continue
    else:
        cnt += 1
        a = n[i]
print(cnt + 1)
