import numpy as np
S=np.array(list(input()),dtype=np.int8)
L=len(S)
A=np.arange(L)&1
B=1-A
x1=(A!=S).sum()
x2=(B!=S).sum()
print(min(x1,x2))
