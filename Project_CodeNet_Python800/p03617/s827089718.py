import sys

input = sys.stdin.readline
MOD = 1000000007

Q,H,S,D = map(int,input().split())
N = int(input())

#1L min
min_1L = min(min(4*Q,2*H),S)

min_2L = min(D,2*min_1L)

#num of 2L
print(N//2*min_2L + N%2*min_1L)