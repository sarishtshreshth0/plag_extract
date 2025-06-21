from collections import Counter

N,*D = map(int, open(0).read().split())
m = 998244353
if D[0] > 0:
    print(0)
else:
    dc = Counter(D)
    dci = [x for x in dc.items()]
    ans = 1
    if dc[0] > 1:
        print(0)
    else:
        for i in range(1,max(dci)[0]+1):
            if dc[i] == 0:
                print(0)
                break
            else:
                ans = (ans*pow(dc[i-1],dc[i],m)) % m
        else:
            print(ans)