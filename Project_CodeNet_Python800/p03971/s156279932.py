n,a,b=map(int,input().split())
s=input()
participant=[str(c) for c in s]
gokakua=0
gokakub=0
for i in participant:
    if i=='a':
        if gokakua+gokakub<a+b:
            print("Yes")
            gokakua+=1
        else:
            print("No")
    if i=='b':
        if gokakua+gokakub<a+b and gokakub<b:
            print("Yes")
            gokakub+=1
        else:
            print("No")
    if i=='c':
        print("No")