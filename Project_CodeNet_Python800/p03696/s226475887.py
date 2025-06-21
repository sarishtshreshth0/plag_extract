n = int(input())
s = input()
ans = s
while s.count("()")>0:
    s = s.replace("()", "")
cnt_l = s.count(")")
cnt_r = s.count("(")
ans = cnt_l * "(" + ans
ans += cnt_r * ")"
print(ans)