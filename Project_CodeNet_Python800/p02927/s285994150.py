import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    M,D=MI()
    ans=0
    for m in range(1,M+1):
        for d in range(1,D+1):
            d1=d%10
            d2=d//10
            
            if d1>=2 and d2>=2:
                if m==d1*d2:
                    ans+=1
                    
    print(ans)
                

main()
