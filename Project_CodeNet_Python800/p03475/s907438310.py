N = int(input())
CSF = [list(map(int,input().split())) for i in range(N-1)]

for j in range(0,N,1):
    t = 0
    for i in range(j,N-1,1):
        C,S,F = CSF[i]

        if t < S:#まだ１ポンも出てないなら待つしかない
            t = S
        
        if t%F != 0:
            t += F-t%F
        
        t += C

    print(t)
    
