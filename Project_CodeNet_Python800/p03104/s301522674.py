from sys import stdin
def main():
    #入力
    readline=stdin.readline
    a,b=map(int,readline().split())

    if a==0:
        print(f(b))
    else:
        print(f(b)^f(a-1))

def f(n):
    if n%4==3:
        return 0
    elif n%4==2:
        return n^1
    elif n%4==1:
        return 1
    else:
        return n

if __name__=="__main__":
    main()