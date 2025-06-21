s=input()
a,b=0,0
for i in range(len(s)):
    if i%2==0 and s[i]=="1":
        a+=1
    elif i%2==1 and s[i]=="0":
        a+=1
for i in range(len(s)):
    if i%2==0 and s[i]=="0":
        b+=1
    elif i%2==1 and s[i]=="1":
        b+=1
print(min(a,b))