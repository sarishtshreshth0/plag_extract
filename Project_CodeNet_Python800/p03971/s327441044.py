num, a ,b = map(int,input().split())
s = input()
a_cnt = 0
b_cnt = 0
for i in range(num):
    if s[i] == "a" and a_cnt + b_cnt < a + b:
        print("Yes")
        a_cnt += 1
    elif s[i] == "b" and a_cnt + b_cnt < a + b and b_cnt < b:
        print("Yes")
        b_cnt += 1
    else:
        print("No")

