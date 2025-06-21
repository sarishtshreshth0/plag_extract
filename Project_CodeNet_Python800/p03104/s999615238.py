A,B=map(int,input().split())
B+=1
Abit=[0]*41
for j in range(41):
    bitp=A//(2*(2**j))
    bitm=A%(2*(2**j))
    Abit[j]+=bitp*(2**j)
    Abit[j]+=max(0,bitm-2**j)
Bbit=[0]*41
for j in range(41):
    bitp=B//(2*(2**j))
    bitm=B%(2*(2**j))
    Bbit[j]+=bitp*(2**j)
    Bbit[j]+=max(0,bitm-2**j)
res=0
for j in range(41):
    Bbit[j]-=Abit[j]
    res+=(Bbit[j]%2)*(2**j)
print(res)
