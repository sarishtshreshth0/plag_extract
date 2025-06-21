n=int(input())
s=str(input())

ans=0#(
count1=0
for i in range(n):
    if s[i]=='(':
        count1+=1
    else:
        if count1==0:
            ans+=1
        else:
            count1-=1

for i in range(ans):
    print('(',end="")
print(s,end="")
for i in range(count1):
    print(')',end="")
