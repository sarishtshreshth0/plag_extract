M,D = map(int,input().split())

c = 0

for m in range(1,M+1):
    for d in range(20,D+1):
        if(d%10 >= 2):
            if(m == (d//10)*(d%10)):c += 1
print(c)