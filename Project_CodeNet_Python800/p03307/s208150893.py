import math
def main():
    n=int(input())
    x=2*n//math.gcd(2,n)
    print(x)
    
if __name__ == "__main__":
    main()