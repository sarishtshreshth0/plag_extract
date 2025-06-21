A,B=map(int,input().split())
A=(A-2)%13
B=(B-2)%13
print(['Draw','Alice','Bob'][(A>B)-(B>A)])