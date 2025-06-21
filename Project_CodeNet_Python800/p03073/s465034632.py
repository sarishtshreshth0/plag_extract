from copy import deepcopy
s1 = list(input())
s2 = deepcopy(s1)
length = len(s1)

ans1 = 0
ans2 = 0

# 1文字目'0'
for a in range(length):
    if a % 2 == 0:
        if s1[a] == '1':
            s1[a] = '0'
            ans1 += 1
    else:
        if s1[a] == '0':
            s1[a] = '1'
            ans1 += 1

# 1文字目'1'
for a in range(length):
    if a % 2 == 0:
        if s2[a] == '0':
            s2[a] = '1'
            ans2 += 1
    else:
        if s2[a] == '1':
            s2[a] = '0'
            ans2 += 1

print(min(ans1, ans2))
