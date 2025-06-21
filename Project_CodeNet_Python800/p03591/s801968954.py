

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    s=input()
    if s[:4]=="YAKI":
        print("Yes")
    else:
        print("No")

main()
