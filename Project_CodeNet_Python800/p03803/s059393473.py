A,B = (int(T) for T in input().split())
if A==1 or B==1:
    print(['Alice','Draw','Bob'][(A>B)+(A>=B)])
else:
    print(['Alice','Draw','Bob'][(A<B)+(A<=B)])