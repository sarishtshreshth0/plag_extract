N=int(input())
temp=N
f=0
for i in range(8):
    f+=N%10
    N-=N%10
    N=N//10

if temp%f==0:
    print("Yes")
else:
    print("No")
