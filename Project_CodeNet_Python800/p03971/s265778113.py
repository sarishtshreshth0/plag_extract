n,a,b=map(int,input().split())
s=input()

ninzu=0
kaigai=0
ans=0
for s_i in s:
    if s_i=='a':
        if ninzu<(a+b):
            print('Yes')
            ninzu+=1
        else:
            print('No')
    if s_i=='b':
        if ninzu<(a+b) and kaigai<b:
            print('Yes')
            ninzu+=1
            kaigai+=1
        else:
            print('No')
    if s_i=='c':
        print('No')

