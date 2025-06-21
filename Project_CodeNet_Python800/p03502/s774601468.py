n=input()
L=[int(n) for n in list(str(n))]
print("YNeos"[int(n)%sum(L)!=0::2])