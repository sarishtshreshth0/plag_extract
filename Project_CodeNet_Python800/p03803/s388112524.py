a,b=map(int,input().split())
A=14 if a==1 else a
B=14 if b==1 else b
print('Draw' if A==B else 'Alice' if A>B else 'Bob')
