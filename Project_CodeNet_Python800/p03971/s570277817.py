S=lambda:input()
I=lambda:int(input())
L=lambda:list(map(int,input().split()))
LS=lambda:list(map(str,input().split()))

n,a,b=L()
s=S()
passed=0
rankbyb=0
for i in range(n):
    if s[i]=='b':
        rankbyb+=1
        
    if s[i]=='a' and passed<a+b:
        print('Yes')
        passed+=1
    elif s[i]=='b' and passed<a+b and rankbyb<=b:
        print('Yes')
        passed+=1
    else:
        print('No')