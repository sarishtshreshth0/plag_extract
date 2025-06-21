import math

n = int(input())
set = []
i = 1
ans = []

t = n**0.5
if len(str(t)) <=8:
    print(len(str((math.floor(t)))))
else:
    while i*i <= n:
        cc = []
        pre = []
        if n % i == 0:
            pre.append(i)
            cc.append(len(str(i)))
            if i != n // i:
                pre.append(n//i)
                cc.append(len(str(n//i)))
                if cc == []:
                    continue
                else:
                    ans.append(pre)
                    result = abs(cc[0]-cc[1])
                    set.append(result)

        i += 1


    min = set.index(min(set))
    print(len(str((max(ans[min])))))



