N=int(input())

Station=[]
for n in range(N-1):
    Station.append(list(map(int,input().split())))
    
S=range(N)
for i in range(len(S)):
    t=0
    for s in range(i,len(S)-1):
        if t <= Station[s][1]:
            t = Station[s][1] + Station[s][0]
        else:
            if t%Station[s][2] != 0:
                t = t + (Station[s][2]-t%Station[s][2]) + Station[s][0]
            else:
                t = t + Station[s][0]
    print(t)