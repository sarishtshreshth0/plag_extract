A,B = map(int, input().split())

fa = 0
if A%2 == 0 and A%4 == 0:
    fa = 0
elif A%2 == 0 and A%4 != 0:
    fa = 1
elif A%2 != 0 and (A-1)%4 == 0:
    fa = ((A-1) ^ 0)
elif A%2 != 0 and (A-1)%4 != 0:
    fa = (A-1) ^ 1

fb = 0
if (B+1)%2 == 0 and (B+1)%4 == 0:
    fb = 0
elif (B+1)%2 == 0 and (B+1)%4 != 0:
    fb = 1
elif (B+1)%2 != 0 and B%4 == 0:
    fb = (B ^ 0)
elif (B+1)%2 != 0 and B%4 != 0:
    fb = (B ^ 1)

print(fa ^ fb)