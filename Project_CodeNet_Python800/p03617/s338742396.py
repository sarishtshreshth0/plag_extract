q,h,s,d = map(int,input().split())

n = int(input())

price = [q,h,s,d]
base = [8,4,2,1]
quant = [1,2,4,8]

comp = []
for i in range(4):
    comp.append([price[i]*base[i],i])

comp.sort()
# print(comp)

ans = 0
n *= 4

for ind in range(4):
    tag = comp[ind][1]
    p = price[tag]
    q = quant[tag]
    pos = n//q
    # print(pos)
    if pos >= 0:
        ans += p*pos
        n -= q*pos
    else:
        continue

print(ans)