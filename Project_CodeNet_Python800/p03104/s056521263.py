a,b = map(int,input().split())
if a==0:
    print(b)
    exit()
ab = bin(a-1)[2:]
bb = bin(b)[2:]
# print(ab)
# print(bb)
sa = []
sb = []
if int(bb[-1]):
    sb = [1]
else:
    for i in bb:
        sb += [int(i)]
if a>0:
    if int(ab[-1]):
        sa = [1]
    else:
        for i in ab:
            # print(2)
            sa += [int(i)]
sa[-1] = (a//2)%2
sb[-1] = ((b+1)//2)%2
# print(sa)
# print(sb)
# print(ab)
ta = "".join([str(i) for i in sa])
tb = "".join([str(i) for i in sb])
ta = int(ta,2)
tb = int(tb,2)
# print(ta)
# print(tb)
ans = ta^tb
# print(ta)
# print(tb)
print(ans)