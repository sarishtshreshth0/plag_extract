n = int(input())
li = list(map(int,input().split()))
if li[0]!=0:
    print(0)
    exit()

import collections
c = collections.Counter(li)

#print(c)
# Counter({'a': 4, 'c': 2, 'b': 1})
#print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])

tmp = c.items()
cnt = list(tmp)
cnt.sort()
#print(cnt)
#[(0, 1), (1, 2), (2, 3), (3, 1)]
ans = 1
for i,c in enumerate(cnt):
    if i == 0:
        if c[1]>=2:
            print(0)
            exit()
        continue
    if c[0]!= i:
        print(0)
        exit()
    #print(cnt[i-1][1],c[1])
    ans *= cnt[i-1][1]**c[1]
print(ans%998244353)