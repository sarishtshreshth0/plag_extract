a, b, c = list(map(int, input().rstrip().split()))
if (c >= a and c <= b) or (c >= b and c <= a):
    print("Yes")
else:
    print("No")