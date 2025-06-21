n=int(input())

for a in range(1,int(n**0.5+1)):
    if n%a==0:
        b=n//a
        sa=str(a)
        sb=str(b)
        if a<=b:
             ans=len(sb)
        else:
            break

print(ans)