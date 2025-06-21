import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
a,b,c = map(int,readline().split())
if a < c < b or a > c > b:
    print("Yes")
else:
    print("No")