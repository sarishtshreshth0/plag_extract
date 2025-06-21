n=int(input())
def f(x):
    z=0
    while x>0:
        z+=x%10
        x=x//10
    return z
print("Yes" if n%f(n)==0 else "No")

