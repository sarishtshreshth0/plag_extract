import collections

N = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
ans = 0
tmp = c.most_common()[0][1]
tmp2 = c.most_common(999999)
for i in range(len(tmp2)):
    tmp3 = tmp2[i][1] + c[tmp2[i][0] + 1] + c[tmp2[i][0] + 2]
    tmp4 = tmp2[i][1] + c[tmp2[i][0] - 1] + c[tmp2[i][0] - 2]
    ans = max(ans,tmp3,tmp4)
print(str(ans))