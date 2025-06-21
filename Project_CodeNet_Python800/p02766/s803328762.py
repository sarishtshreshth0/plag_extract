#Good question
import sys
N,K = map(int,input().split())

if not ( 1 <= N <= 10**9 and 2 <= K <= 10 ): sys.exit()

count = 0
a = N
while a >= K:
    a = a // K
    count += 1
print(count+1)