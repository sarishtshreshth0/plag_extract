n=int(input())
s=input()
a=0
b=0
for i in range(n):
    if s[i]=='(':
        a+=1
    else:
        if a==0:
            b+=1
        else:
            a-=1
print('('*b+s+')'*a)