A,B,C=map(int,input().split())
l=[A,B,C]
l.sort()
#print(l)
if l[1]==C:
    print("Yes")
else:
    print("No")