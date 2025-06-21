def calc(x):
    if x % 4 == 1:
        return 1
    if x % 4 == 3:
        return 0
    
    if x % 4 == 2:
        return 1 + x
    else:
        return x


# 1,5,9,13,... => 1
# 3,7,11,15,... => 0
A, B = map(int, input().split())
x = calc(A - 1)
y = calc(B)
print(x ^ y)
