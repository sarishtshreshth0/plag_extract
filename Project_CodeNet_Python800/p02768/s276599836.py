n,a,b=map(int,input().split())
c=max(a,b)
b=min(a,b)
a=c
MOD = pow(10,9) + 7

X=1
Y=1

for i in range(1,a+1):
    X=X*(n+1-i)%MOD
    Y=Y*i%MOD
    if i==b:
        b_X=X
        b_Y=Y
a_X=X
a_Y=Y
def calc(X,Y,MOD):
    return X*pow(Y,MOD-2,MOD)

ans=pow(2,n,MOD)%MOD-1-calc(a_X,a_Y,MOD)-calc(b_X,b_Y,MOD)

print(ans%MOD)
