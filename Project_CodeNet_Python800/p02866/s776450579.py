def main():
    import sys
    n,*d=map(int,sys.stdin.buffer.read().split())
    e=[0]*n
    for i in d:
        e[i]+=1
    a=1 if d[0]<1 else 0
    for i in d[1:]:a=a*e[i-1]%998244353
    print(a)
main()
