import math
def main():
    n,x=map(int,input().split())
    p=0
    for i in map(int,input().split()):
        p = math.gcd(p, i-x)
    print(p)

if __name__ == "__main__":
    main()