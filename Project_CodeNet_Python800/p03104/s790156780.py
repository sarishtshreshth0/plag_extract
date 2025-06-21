A, B = map(int,input().split(' '))
B += 1
l = "1" if A%4 in [0,1] else "0"
r = "1" if B%4 in [0,1] else "0"
n = 2
while n <= A:
    if A%(2*n)-n <= 0 or A%(2*n)%2 == 0:
        l += "0"
    else:
        l += "1"
    n *= 2
n = 2
while n <= B:
    if B%(2*n)-n <= 0 or B%(2*n)%2 == 0:
        r += "0"
    else:
        r += "1"
    n *= 2
print(int(l[::-1], 2)^int(r[::-1], 2))