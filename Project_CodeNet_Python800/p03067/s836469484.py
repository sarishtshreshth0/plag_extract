a,b,c = map(int,input().split())
for i in range(min(a,b),max(a,b)):
    if i == c:
        print("Yes")
        break
else:
    print("No")