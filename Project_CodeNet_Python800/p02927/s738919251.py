def resolve():
    A, B = map(int, input().split())
    ans = 0
    for i in range(1, A+1):
        for j in range(10, B+1):
            if str(j)[0] != "1" and str(j)[1] != "1":
                if int(str(j)[0])*int(str(j)[1]) == i:
                    ans += 1
    print(ans)
resolve()