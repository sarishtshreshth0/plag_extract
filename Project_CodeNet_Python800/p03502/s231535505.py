n = int(input())

def digits_sum(x):
    
    s = 0
    
    while x>0:
        s += x % 10
        x //= 10
    
    return s
    
if n % digits_sum(n) == 0:
    print("Yes")
else:
    print("No")