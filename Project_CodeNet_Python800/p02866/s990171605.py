import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():




    n = I()
    d = LI()
    mod = 998244353
    
    dcnt = [0]*(max(d)+1)
    

    for x in d:
        dcnt[x] += 1

    nexist = d[0]!=0 or 0 in dcnt or 0 in d[1:]
    if nexist:
        print(0)
        exit(0)

    
    ans = 1

    for i in range(1, len(dcnt)):
        ans *= pow(dcnt[i-1], dcnt[i], mod)
        ans %= mod

    print(ans)
                    


main()
