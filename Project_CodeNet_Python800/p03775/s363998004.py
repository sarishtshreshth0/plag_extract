N=int(input())
if N==1:
    print(1)
    exit()
l=[]
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        l.append(i)
#print(l)
a=l[-1]
b=N//a
s=max(a,b)
print(len(str(s)))