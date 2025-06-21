import sys
def S(): return sys.stdin.readline().rstrip()
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    n,a,b = IL()
    s = S()
    count = 0
    fs = 1
    for rep in s:
        if rep=='a':
            if count < a+b:
                count += 1
                print('Yes')
            else:
                print('No')
        elif rep=='b':
            if count<a+b and fs<=b:
                count += 1
                fs += 1
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    return

if __name__=='__main__':
    solve()