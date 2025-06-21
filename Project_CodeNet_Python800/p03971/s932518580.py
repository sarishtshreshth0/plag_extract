import math
a,b,c = map(int,input().split())
s = input()
g = 1
d = b+c
k = 1
for i in range(a):
    if s[i]=='c':
        print("No")
    elif s[i] == 'a' and k<=d:
        print("Yes")
        k+=1
    elif s[i] == 'b' and g<=c and k<=d:
        print("Yes")
        k+=1
        g += 1
    else:
        print("No")
