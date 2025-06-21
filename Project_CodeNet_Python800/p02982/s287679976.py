
url = "https://atcoder.jp//contests/abc133/tasks/abc133_b"
import itertools
def main():
    n,d = list(map(int, input().split()))
    lis = []
    for i in range(n):
        t = list(map(int, input().split()))
        lis.append(t)
    count = 0
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if i == j:
                continue
            if float.is_integer(ret(lis[i], lis[j])):
                count += 1
    print(count)


import math
def ret(a,b):
    retval = 0
    idx = 0
    while True:
        if idx == len(a):
            break
        retval += abs(a[idx]-b[idx])**2
        idx += 1
    return math.sqrt(retval)

if __name__ == '__main__':
    main()
