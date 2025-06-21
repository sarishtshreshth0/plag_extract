x = int(input())

def div(x):
    r = 0
    while x > 0:
        a = x % 10
        r += a
        x //= 10
    
    return r

t = div(x)
if x % t == 0:
    print("Yes")
else:
    print("No")