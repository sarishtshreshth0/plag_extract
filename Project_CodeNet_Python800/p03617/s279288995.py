from sys import stdin
def main():
    #入力
    readline=stdin.readline
    q,h,s,d=map(int,readline().split())
    n=int(readline())

    if n%2==0:
        print(min(4*q*n,2*h*n,s*n,d*n//2))
    else:
        tmp1=min(4*q*(n-1),2*h*(n-1),s*(n-1),d*(n-1)//2)
        tmp2=min(4*q,2*h,s)
        print(tmp1+tmp2)
        
if __name__=="__main__":
    main()