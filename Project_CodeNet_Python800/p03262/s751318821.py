import sys
import math
def I():return int(sys.stdin.readline().replace("\n",""))
def I2():return map(int,sys.stdin.readline().replace("\n","").split())
def S():return str(sys.stdin.readline().replace("\n",""))
def L():return list(sys.stdin.readline().replace("\n",""))
def Intl():return [int(k) for k in sys.stdin.readline().replace("\n","").split()]
def Lx(k):return list(map(lambda x:int(x)*-k,sys.stdin.readline().replace("\n","").split()))

def gcd(a,b):
    return math.gcd(a,b)

if __name__ == "__main__":
    n,x = I2()
    a = Intl()
    ans = abs(a[0]-x)
    for i in range(1,n):
        ans = gcd(ans,abs(a[i]-x))
    print(ans)
