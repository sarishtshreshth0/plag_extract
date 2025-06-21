# coding: utf-8

m, d = map(int,input().split())

ans = 0
for i in range(1,m+1):#月
    for j in range(1,d+1):#日
        if len(str(j)) == 2:
            d1 = int(str(j)[0])
            d10 = int(str(j)[1])
            if i >= 2 and d1 >= 2 and d10 >= 2 and int(str(j)[0]) * int(str(j)[1]) == i:
                ans += 1

print(ans)