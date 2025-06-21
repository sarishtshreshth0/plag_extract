a,b,c,d = map(int,input().split())
Alice = ['1' if i>=a and i<=b else '0' for i in range(101)]
Bob = ['1' if i>=c and i<=d else '0' for i in range(101)]
ans = 0
for i in range(101):
    if Alice[i]=='1' and Bob[i]=="1":
        ans+=1
print(0 if ans==0 else ans-1)