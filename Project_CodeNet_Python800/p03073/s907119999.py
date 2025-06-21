import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    S = list(input())

    count1 = 0
    count2 =0
    b ="1"
    w ="0"
    for i in range(len(S)):
        if int(S[i]) != i%2:
            count1 +=1
        if int(S[i]) != (i+1)%2:
            count2 +=1
    print(min(count1,count2))





if __name__ == "__main__":
    main()
