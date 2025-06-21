a,b,c = map(int,input().split())
li = [a,b,c]
li.sort()
if li[1] == c:
    print("Yes")
else:
    print("No")