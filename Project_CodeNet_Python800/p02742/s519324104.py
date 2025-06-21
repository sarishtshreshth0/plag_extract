[H,W] = list(map(int,input().split(' ')))
K = int((H*W+1)*0.5)
if H==1 or W==1:print(1)
else:print(K)