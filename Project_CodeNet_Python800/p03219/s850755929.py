import sys


def input():
    return sys.stdin.readline()[:-1]

# N = int(input())
# A = [int(x) for x in input().split()]
# a, b, c = map(int, input().split())
# name1 = str(input())
# alph = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}


a,b=map(int,input().split())
print(a+int(b/2))