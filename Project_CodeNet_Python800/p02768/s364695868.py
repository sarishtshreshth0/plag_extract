# input
n,a,b = list(map(int,input().split()))
p=10**9+7

#全体の組み合わせの数：All
all_ = pow(2,n,p)

#n本からi本選ぶ組み合わせの数:C[i],i:0~b
C_=[1]*(b+10)
for i in range(1,b+1):
    C_[i] = (C_[i-1] * (n-i+1)%p * pow(i,p-2,p))%p 
# C_

ans = (all_-C_[a]-C_[b])%p
print(ans-1)