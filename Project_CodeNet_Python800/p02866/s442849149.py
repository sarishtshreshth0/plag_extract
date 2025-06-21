N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
else:
    tmp = [0 for _ in range(10 ** 5)]
    for i in range(N):
        tmp[D[i]] += 1

    if tmp[0] != 1:
        print(0)
    else:
        ans = 1
        flag = False
        flag2 = False
        for i in range(1, 10 ** 5 - 1):

            if flag2 and tmp[i+1] != 0:
                ans = 0
                break

            if tmp[i+1] == 0:
                flag2 = True

            ans = (ans * (tmp[i] ** tmp[i+1])) % 998244353

        print(ans) 
