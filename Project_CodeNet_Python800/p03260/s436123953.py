a,b = map(int,input().split())
c = 1
while True:
    if a * b * c % 2 == 1:
        print("Yes") 
        break
    elif c == 3:
        print("No")
        break
    else:
        c += 1