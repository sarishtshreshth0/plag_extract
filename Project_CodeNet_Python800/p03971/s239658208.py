n,a,b = map(int,input().split())
s = list(input())

yes_num = 0
gai = 0

for i in s:
    if i == "a":
        if yes_num < a + b:
            yes_num += 1
            print("Yes")
        else:
            print("No")
    
    elif i == "b":
        if yes_num < a+b and gai < b:
            yes_num += 1
            gai += 1
            print("Yes")
        else:
            print("No")
    
    elif i == "c":
        print("No")