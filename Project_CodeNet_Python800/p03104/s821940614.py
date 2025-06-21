a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
def f(a):
    if a % 2 == 0:
        return a ^ (a+1)//2%2
    else:
        return (a+1)//2%2
    
print(f(b) ^ f(a-1))
