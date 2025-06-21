N,X = list(map(int,input().split()))
X_=list(map(int,input().split()))

X_.append(X)
X_.sort()

X_diff=[]
for x_idx in range(1,len(X_)):
    x =X_[x_idx-1]
    x_=X_[x_idx]
    X_diff.append(x_-x)
    
import math
gcd_=X_diff[0]

for x_diff in  X_diff[1:]:
    gcd_=math.gcd(gcd_,x_diff)
    
print(gcd_)