#入力
n,a,b = map(int, input().split())
s = list(input()) #1文字ずつリストに格納する
#総通過人数
pass_contest = 0
#海外学生の順位
rank_overseas = 0
for i in range(len(s)):
    if s[i] == "c":
        print("No")
    elif s[i] == "a" and pass_contest < a+b:
        print("Yes")
        pass_contest += 1
    elif s[i] == "b":
        rank_overseas += 1
        if pass_contest < a+b and rank_overseas <= b:
            print("Yes")
            pass_contest += 1
        else:
            print("No")
    else:
        print("No")