n,a,b=list(map(int, input().strip().split()))
s=input().strip()
x=0
y=0
for i in range(n):
    if s[i]=='a':
        if x<a+b:
            print("Yes")
            x=x+1
        else:
            print("No")
    elif s[i]=='b':
        if x<a+b and y<b:
            print("Yes")
            x=x+1
            y=y+1
        else:
            print("No")
    else:
        print("No")