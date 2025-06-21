i = list(map(int,input().split()))

if(i[0] < i[1]):
    if(i[0] < i[2] and i[2] < i[1]):
        print("Yes")
    else:
        print("No")

elif(i[0] > i[1]):
    if(i[1] < i[2] and i[2] < i[0]):
        print("Yes")
    else:
        print("No")

else:
    print("No")