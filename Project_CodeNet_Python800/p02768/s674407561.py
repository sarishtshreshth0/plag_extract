#

import sys
input=sys.stdin.readline
MOD=10**9+7

def main():
    n,a,b=map(int,input().split())
    nca=1
    for i in range(a):
        nca=(nca*(n-i))%MOD
    for i in range(a):
        nca=(nca*pow(i+1,MOD-2,MOD))%MOD
    ncb=1
    for i in range(b):
        ncb=(ncb*(n-i))%MOD
    for i in range(b):
        ncb=(ncb*pow(i+1,MOD-2,MOD))%MOD
    print((pow(2,n,MOD)-1-nca-ncb)%MOD)
    
    
    
if __name__=="__main__":
    main()
