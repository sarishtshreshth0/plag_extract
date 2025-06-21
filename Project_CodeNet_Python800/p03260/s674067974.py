A,B =map(int,input().split())
for i in range(1,4,1):
    if (A*B*i) %2 ==1:
        print("Yes")
        exit()
print("No")


