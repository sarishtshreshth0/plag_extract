from sys import stdin
N=list(map(int,stdin.readline().strip().split()))[0]
eki=[list(map(int,input().split())) for _ in range(N-1)]

for i in range(len(eki)):
    x = eki[i][1]+eki[i][0]
    for j in range(i+1,len(eki)):
        if eki[j][1] >x:
            x=eki[j][1]
            x += eki[j][0]
        elif x%eki[j][2]==0:x+=eki[j][0]
        else:
            x+=eki[j][0]+eki[j][2]-x%eki[j][2]
    print(x)
print(0)