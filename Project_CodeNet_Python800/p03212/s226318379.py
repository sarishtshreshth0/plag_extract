import collections
n = int(input())
dic = collections.defaultdict(int)
ans = 0
if n < 357:
    print(0)
else:
    ls = ["357","375","537","573","735","753"]
    ls_next = []
    for i in range(len(ls)):
        if int(ls[i]) <= n:
            ls_next.append(ls[i])
    ls = ls_next
    ans += len(ls_next)
    for i in range(10):
        ls_next = []
        for j in range(len(ls)):
            for k in range(len(ls[0])):
                if int(ls[j][:k]+"3"+ls[j][k:]) <= n:
                    ls_next.append(ls[j][:k]+"3"+ls[j][k:])
                if int(ls[j][:k]+"5"+ls[j][k:]) <= n:
                    ls_next.append(ls[j][:k]+"5"+ls[j][k:])
                if int(ls[j][:k]+"7"+ls[j][k:]) <= n:
                    ls_next.append(ls[j][:k]+"7"+ls[j][k:])
        for j in range(len(ls_next)):
            dic[ls_next[j]] = 1
        ls_next = list(dic.keys())
        #print(ls_next)
        if len(ls_next) == 0:
            break

        ans += len(ls_next)
        ls = ls_next
        dic.clear()
    print(ans)
