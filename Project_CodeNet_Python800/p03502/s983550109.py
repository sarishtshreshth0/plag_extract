n=input()
a=int(n)
n=[int(i) for i in n]
if a%sum(n)==0:
    print("Yes")
else:
    print("No")