import math

def resolve():
    M,D=map(int,input().split())

    cnt=0
    for m in range(1,M+1):
        for d in range(1,D+1):
            if(d//10 < 2 or d%10 <2):
                continue
            if((d%10) * (d//10) == m):
                cnt+=1

    print(cnt)


resolve()