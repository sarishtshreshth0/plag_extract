INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    n=INT()
    if n%2==0:
        print(n)
    else:
        print(2*n)
if __name__ == '__main__':
    do()