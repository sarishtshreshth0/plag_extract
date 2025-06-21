import sys
import math
import itertools


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    A = int(math.log10(N))
    flag=0
    count =0
    for a in range(3,A+2):

        for i in itertools.product([3,5,7],repeat=a):
            digit=0
            if 3 in i and  5 in i and 7 in i:


                for s in range(a):
                    digit+=10**(a-s-1)*i[s]
                if digit <=N:
                    count+=1
                else:
                    break
    print(count)


if __name__ == "__main__":
    main()
