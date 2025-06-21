s = input()


e0=e1=o0=o1=0
for i in range(len(s)):
    if s[i]=="0" :
        if i%2!=0 :
            e0+=1
        else:
            o0+=1
    else:
        if i%2!=0 :
            e1+=1
        else:
            o1+=1

# print(e0,e1,o0,o1)
ot = len(s)//2 if len(s)%2==0 else (len(s)+1)//2
et = len(s)//2

ans = min(abs(e0-et)+abs(o1-ot),abs(e1-et)+abs(o0-ot))
print(ans)

