import math
def diff(l):
    c = 0
    ans = []
    for i in l:
        try:
            ans.append(abs(i-l[c+1]))
            c+=1
        except:
            continue
    return ans
def multiGCD(l):
    ans = 0
    for i in l:
        ans = math.gcd(ans, i)
    return ans
n, x = map(int, input().split())
l = list(map(int, input().split()))
l.append(x)
l.sort()
l2 = diff(l)
print(multiGCD(l2))