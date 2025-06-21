n=int(input())
l=[]
for i in range(n):
    w=input()
    if len(l)==0:
        l.append(w)
        old_w=w[-1]
    else:
        if (w in l) or (old_w!=w[0]):
            print("No")
            exit()
        else:
            l.append(w)
            old_w=w[-1]
print("Yes")