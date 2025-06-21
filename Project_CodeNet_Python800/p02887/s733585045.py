n=int(input())
s=str(input())
l=[]
for i in range(0,len(s)):
    if(len(l)==0):
        l.append(s[i])
    elif(l[len(l)-1]!=s[i]):
        l.append(s[i])
    else:
        pass
print(len(l))