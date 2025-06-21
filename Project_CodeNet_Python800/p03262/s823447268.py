import numpy as np
import bisect
def main():
    n,X = map(int,input().split())
    x = [int(i) for i in input().split()]
    index = bisect.bisect_left(x,X)
    x.insert(index,X)
    diff = []
    for i in range(1,n+1):
        diff.append(x[i]-x[i-1])
    diff = np.array(diff)
    ans = np.gcd.reduce(diff)
    print(ans)
main()
