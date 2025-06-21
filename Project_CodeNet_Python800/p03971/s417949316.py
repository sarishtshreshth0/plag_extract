N, A, B = map(int, input().split())
S = input()

mem = list(S)
now = 0
fore=1
for i in range(N):
    if(mem[i]=='a'):
        if(now<(A+B)):
            now+=1
            print('Yes')
        else:
            print('No')

    elif(mem[i]=='b'):
        if(now<(A+B)):
            if(fore<=B):
                fore+=1
                now+=1
                print('Yes')
            else:
                print('No')
        else:
            print('No')

    else:
        print('No')
