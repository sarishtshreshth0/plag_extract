a,b,c,d = list(map(int,input().split()))

l_ab = []
l_cd = []
for i in range(a,b+1):
    l_ab.append(i)
for i in range(c,d+1):
    l_cd.append(i)


print(max(0,len(set(l_ab)&set(l_cd))-1))