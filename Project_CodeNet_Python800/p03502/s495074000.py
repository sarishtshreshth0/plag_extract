n=list(input())
suzi=int("".join(n))
for i in range(len(n)):
    n[i]=int(n[i])
if suzi%sum(n)==0:
    print("Yes")
else:
    print("No")