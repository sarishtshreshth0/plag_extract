s = input()

ans0 = 0
ans1 = 0
for i, s_i in enumerate(s):
    if i % 2 == 0:
        if s_i == '0':
            ans1 += 1
        else:
            ans0 += 1
    else:
        if s_i == '0':
            ans0 += 1
        else:
            ans1 += 1
print(min(ans0, ans1))
