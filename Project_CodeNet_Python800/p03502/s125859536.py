n = input()
fx = sum(list(map(int,list(n))))
if int(n)%fx == 0:
    print("Yes")
else:
    print("No")