a, b, c, d = list(map(int, input().split()))
list = sorted([a, b, c, d])
if list[0] == a and list[1] == b or list[2] == c and list[3] == d:
    print(0)
elif list[0] == c and list[1] == d or list[2] == a and list[3] == b:
    print(0)
else:
    print(list[2] - list[1])