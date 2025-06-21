n,a,b=list(map(int,input().split()))
s=input()
ab=a+b
total=0
foreigner=0
for i in range(n):
    if s[i]=='a':
        if total < ab:
            total+=1
            print("Yes")
        else:
            print("No")
    elif s[i]=='b':
        if total < ab and foreigner < b:
            total+=1
            foreigner+=1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
