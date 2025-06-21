n=int(input())
List=list(str(n))
List=[int(List[i]) for i in range(len(List))]
f_x=sum(List)
if n%f_x==0:
    print("Yes")
else:
    print("No")