def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
q,h,s,d = iim()
n = ii()

if q*8 <= min(4*h,2*s,d):
    print(n*4*q)
elif 4*h <= min(2*s,d):
    print(n*2*h)
elif s*2 <= d:
    print(n*s)
else:
    print(n//2*d + n%2*min(s,2*h,4*q))