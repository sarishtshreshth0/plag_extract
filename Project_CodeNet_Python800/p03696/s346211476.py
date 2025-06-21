n=int(input())
s=list(input())
a=0
b=0
c=0
for i in range(n):
    d=s[i]
    if d=='(':
        a+=1
    else:
        b+=1
        if b-c>a:
            c+=1
print('('*c+''.join(s)+')'*(a-b+c))
