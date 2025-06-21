# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    S=input()
    a,b=0,0
    for i in range(N):
        if S[i]=='(':
            b+=1
        else:
            if b==0:
                a+=1
            else:
                b-=1
    print('('*a+S+')'*b)
            

if __name__ == '__main__':
    main()
