M,D = map(int,input().split())
cnt = 0
for m in range(4,M+1):
    for d in range(1,D+1):
        if d>=20:
            d = str(d)
            if int(d[1])>=2:
                if m==int(d[0])*int(d[1]):
                    cnt += 1
print(cnt)