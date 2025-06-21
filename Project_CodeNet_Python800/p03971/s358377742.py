N, A, B = map(int, input().split())
S = str(input())
a = b = 0
for i in range(N):
    
    if S[i] == 'a':
        a += 1
        if a + b <= A + B:
            print('Yes')
        else:
            print('No')
            a -= 1
    elif S[i] == 'b':
        b += 1
        if a + b <= A + B and b <= B:
            print('Yes')
        else:
            print('No')
            b -= 1
    else:
        print('No')
