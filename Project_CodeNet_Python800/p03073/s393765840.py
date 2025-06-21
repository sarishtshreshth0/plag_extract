s = input()

cnt1, cnt2 = 0, 0
for i in range(len(s)):
    if int(s[i]) == i%2:
        cnt1 += 1
    else:
        cnt2 += 1

print(min(cnt1, cnt2))