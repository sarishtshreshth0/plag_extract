n = int(input())
s = input()
l_cnt = 0
r_cnt = 0
l_ans = 0
for i in s:
    if i == ')':
        if l_cnt:
            l_cnt -= 1
        else:
            l_ans += 1
    else:
        l_cnt += 1

print(l_ans*'(' + s + l_cnt*')')