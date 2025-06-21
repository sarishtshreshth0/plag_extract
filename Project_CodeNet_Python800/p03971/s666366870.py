# B - Qualification simulator
N,A,B = map(int,input().split())
S = input()
domestic,foreign = 0,0

for i in range(N):
    s = S[i]
    if s=='a':
        if domestic+foreign<A+B:
            print('Yes')
            domestic += 1
        else:
            print('No')
    elif s=='b':
        if domestic+foreign<A+B and foreign<B:
            print('Yes')
            foreign += 1
        else:
            print('No')
    else:
        print('No')