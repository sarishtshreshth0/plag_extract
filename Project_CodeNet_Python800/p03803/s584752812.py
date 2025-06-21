A,B = map(int,input().split())

print('Draw' if A ==B else 'Alice' if (A+13)%15 > (B+13)%15 else 'Bob')