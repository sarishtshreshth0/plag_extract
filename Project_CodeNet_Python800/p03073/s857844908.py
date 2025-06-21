import numpy as np
S=list(input())
S=[True if i=="0" else False for i in S]
stripeA=[True]*len(S)
stripeB=[True]*len(S)
for i in range(len(S)):
    if i%2==0:
        stripeA[i]=False
    else:
        stripeB[i]=False
stripeA=list(np.logical_xor(S,stripeA))
stripeB=list(np.logical_xor(S,stripeB))
stripeA=stripeA.count(True)
stripeB=stripeB.count(True)
if stripeA>stripeB:
    print(stripeB)
else:
    print(stripeA)