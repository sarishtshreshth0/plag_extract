N = list(map(int,input().split()))#array = list(map(int, input().strip().split()))
job = list(input())

AB = N[1] + N[2]
x = 0
y = 0

for i in range(N[0] ):
    if job[i] == "a":
        if x < AB:
            x += 1
            print("Yes")
        else:
            print("No")
    
    elif job[i] == "b":
        if x < AB and y < N[2]:
            x += 1
            y += 1
            print("Yes")
        else:
            print("No")
            
    elif job[i] == "c":
        print("No")