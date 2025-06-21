H,W=map(int,input().split())

import sys
N=1
if W==1 or H==1:
    print(1)
    sys.exit()
if (W-1)%2==0:
    N+=(W-1)//2
    N+=(W-1)//2
elif (W-1)%2==1:
    N+=(W-2)//2
    N+=W//2
if H%2==0:
    NN=N*(H//2)
elif H%2==1:
    if (W-1)%2==0:
        NN=N*((H-1)//2)+(W-1)//2+1
    elif (W-1)%2==1:
        NN=N*((H-1)//2)+(W-2)//2+1
print(NN)