a,b = map(int,input().split())
def f(x):
    if (x+1)//2 % 2 == 0:
        ans = 0
    else:
        ans = 1
    if x % 2 == 0:
        ans ^= x
    return ans
print(f(a-1)^f(b))