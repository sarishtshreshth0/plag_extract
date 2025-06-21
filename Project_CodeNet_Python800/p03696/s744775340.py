n = int(input())
s = input()

r_cnt, l_cnt = 0, 0
for i in range(n):
    if s[i] == "(":
        r_cnt += 1
    else:
        if r_cnt == 0:
            l_cnt += 1
        else:
            r_cnt -= 1

print(l_cnt * "(" + s + r_cnt * ")")