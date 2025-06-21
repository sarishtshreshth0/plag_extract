li = list(map(int,input().split()))
s=list(input())
N=li[0]
A=li[1]
B=li[2]
domPass=0
forePass=0
for x in s:
    if(x=='a'):
        if((domPass+forePass)<(A+B)):
            domPass=domPass+1
            print('Yes')
        else:
            print('No')
    elif(x=='b'):
        if(((domPass+forePass)<(A+B))and(forePass<B)):
            forePass=forePass+1
            print('Yes')
        else :
            print('No')
    elif(x=='c'):
        print('No')