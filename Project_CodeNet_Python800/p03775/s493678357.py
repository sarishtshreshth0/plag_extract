def F(x,y):
    x = str(x)
    y = str(y)
    return max(len(x),len(y))
N = int(input())
cmin = 100
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        cmin = min(cmin,F(i,N//i))
print(cmin)