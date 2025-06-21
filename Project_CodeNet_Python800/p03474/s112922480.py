a,b=map(int,input().split())
s=input()
s=s.split('-')
if len(s)!=2 or len(s[0])!=a or len(s[1])!=b:
    print('No')
    exit()
print('Yes')
