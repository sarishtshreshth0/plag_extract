import sys
X = int(input())

if not ( 0 <= X <= 10**9 and isinstance(X,int)): sys.exit

print((X // 500) * 1000 + (( X % 500 ) // 5) * 5)