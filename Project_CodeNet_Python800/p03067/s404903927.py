import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    L=LI()
    if L[2]==(sum(L) - min(L) - max(L)):
        print("Yes")
    else:
        print("No")

main()
