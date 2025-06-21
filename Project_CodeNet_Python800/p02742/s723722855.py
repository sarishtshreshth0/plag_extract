a = input("").split(" ")
a = [int(aa) for aa in a]
H = a[0]
W = a[1]
if H == 1 or W == 1:
    print("1")
elif H % 2 == 0:
    print(str(int(H/2)*W))
elif W % 2 == 0:
    print(str(int(W/2)*H))
else:
    p = int((H+1)/2)
    q = int((W+1)/2)
    print(str(p*q+(p-1)*(q-1)))