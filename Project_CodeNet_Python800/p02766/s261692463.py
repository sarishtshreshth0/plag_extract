N,K=map(int,input().split())
count = 1
kai = K
while N >= K:
    K = K*kai
    count += 1
print(count)