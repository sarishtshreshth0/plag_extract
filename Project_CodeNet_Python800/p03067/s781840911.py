a, b, c = map(int, input().split(" "))
if sorted([a,b])[0] < c and c < sorted([a,b])[1]:
    print("Yes")
else:
    print("No")