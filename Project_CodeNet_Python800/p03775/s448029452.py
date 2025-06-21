N=int(input())
def f(n):
    for i in range(int(n**.5),0,-1):
        if n%i==0:
            return n//i
print(len(str(f(N))))