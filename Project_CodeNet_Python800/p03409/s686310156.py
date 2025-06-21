def main():
    N = int(input())
    # 赤が青の左下にあるようなペアを最大幾つとれるか
    # 全ての点のx,yそれぞれが同じ値になる事はない
    # bluesの左側から見ていって、その点より左下のredsがあるならその中でyが一番大きいものをとる
    reds,blues = [],[]
    for i in range(N):
        a,b = map(int,input().split())
        reds.append([a,b])
    for i in range(N):
        c,d = map(int,input().split())
        blues.append([c,d])
    reds = sorted(reds, key=lambda x:-x[1])
    blues = sorted(blues, key=lambda x:x[0])
    ans = 0
    for i in range(N):
        flag = False
        for j,r in enumerate(reds):
            if blues[i][0]>r[0] and blues[i][1]>r[1]:
                flag = True
                reds.pop(j)
                ans += 1
                break
    print(ans)

main()
