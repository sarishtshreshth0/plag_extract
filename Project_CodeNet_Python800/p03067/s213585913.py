a = list(map(int,input().split()))



if a[2]>a[0] and a[2]<a[1]:
    print("Yes")
elif a[1]<a[2] and a[2]<a[0]:
    print("Yes")
else:
    print("No")