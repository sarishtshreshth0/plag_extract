
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    cnt=0
    N=I()
    S=input()
    now="A"
    for i in range(N):
        if S[i]!=now:
            cnt+=1
        now=S[i]
        
    print(cnt)

main()
