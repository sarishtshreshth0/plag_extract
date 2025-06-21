import math
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

def main():
    A,B=mi()

    x_sum = 0
    ev_cnt = 0
    if A % 2 == 0:
        if B%2==0:
            x_sum ^=B
            ev_cnt = B//2-A//2 
        else:
            ev_cnt = math.ceil(B/2)-A//2 
             
    else:
        if B%2==0:
            x_sum ^=B
            x_sum ^= A
            ev_cnt = B//2-math.ceil(A/2)
        else:
            x_sum ^= A
            ev_cnt = math.ceil(B/2)-math.ceil(A/2)
    

    if ev_cnt % 2 == 0:
        print(x_sum)
    else:
        print(x_sum^1)

if __name__ == "__main__":
    main()