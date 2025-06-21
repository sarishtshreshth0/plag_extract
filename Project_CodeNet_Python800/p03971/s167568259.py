N,A,B = map(int, input().split())
na = nb = 0
S = list(input())
for c in S:
    #print(na,nb,end='')
    if c == 'a':
        na += 1
        if na + nb <= A + B:
            print('Yes')
        else:
            print('No')
        
    elif c == 'b':
        nb += 1
        if na + nb <= A + B and nb <= B:
            print('Yes')
        else:
            nb -= 1
            print('No')
       
    else:
        print('No')

