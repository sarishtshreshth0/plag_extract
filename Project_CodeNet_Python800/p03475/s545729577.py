import math
n = int(input())
all_li = []
for _ in range(n-1):
    tmp_li = list(map(int,input().split()))
    all_li.append(tmp_li)
if n == 1:
    tmp = all_li[0]
    print(tmp[0]+tmp[1])
    exit()
for i,a in enumerate(all_li):
    now = a[1]+a[0]
    #print(i,now,all_li[i+1:])
    for aa in all_li[i+1:]:
        x,y,z = (aa[0],aa[1],aa[2])
        if now <= y:
            now = y+x
        else:
            now = math.ceil((now-y)/z)*z + y + x
    print(now)
    now = 0
print(0)