a, b = map(int, input().split())
def f(x):
    if x%2: return-(-x//2)%2
    else: return (x//2)%2+x
print(f(a-1)^f(b))