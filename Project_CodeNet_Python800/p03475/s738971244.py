import sys
import itertools
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N =int(input())

    C =[]
    S =[]
    F =[]
    for i in range(N-1):
        c,s,f = map(int,input().split())
        C.append(c)
        S.append(s)
        F.append(f)

    for i in range(N-1):
        t = i
        time=0
        while t<N-1:

            if time <=S[t]:
                time =S[t]+C[t]
            else:
                if time %F[t] ==0:
                    time +=C[t]
                else:
                    div = time //F[t]
                    time = (div+1) *F[t] + C[t]
            t+=1

        print(time)

    print(0)





if __name__ == "__main__":
    main()
