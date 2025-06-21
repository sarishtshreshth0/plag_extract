N,S = open(0).read().split()
o = 0
c = 0
pre = 0
temp_o = 0
for b in S:
    if b == '(':
        o += 1
        temp_o += 1
    else:
        c += 1
        if temp_o == 0:
            pre += 1
        else:
            temp_o -= 1
suf = max(0,pre+o-c)
ans = ('('*pre) + S + (')'*suf)
print(ans)