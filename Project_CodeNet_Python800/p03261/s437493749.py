n=int(input())
l=[]
l.append(input())
for i in range(1,n):
    w=input()
    if w in l or l[i-1][-1]!=w[0]:
        print("No")
        exit()
    else:
        l.append(w)
print("Yes")




