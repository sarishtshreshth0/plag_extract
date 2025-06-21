import fractions
N,X = map(int,input().split())

x = list(map(int,input().split()))
st = []
x.append(X)

x.sort()

gcd = 0

for i in range(N):
    if i == 0:
        gcd = x[i+1]-x[i]
    else:
        gcd = fractions.gcd(gcd,x[i+1]-x[i])
    st.append(x[i+1]-x[i])
print(gcd)

