n = int(input())
ary = list(map(int, input().split()))
#print(n,ary)

ary_2 = [ary[0]]
for i in range(1, n):
    ary_2.append(ary[i] + ary_2[i-1])
ary_2 = [0] + ary_2
#print(ary_2)

from collections import Counter #総当たり二重ループでは'TLE'
c = Counter(ary_2)
v = (c.values())
#print(v)

ans = 0
for j in v:
    if j > 1:
        ans += j * (j-1) // 2 # 'J'個から'2'個選ぶ場合の数_combination, 重複無し

print(ans)
