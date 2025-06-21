import sys
A,B,C,D = map(int,input().split())
if A < 0 or B < 0 or B <= A or A > 100 or B > 100:
    sys.exit()
if C < 0 or D < 0 or D <= C or C > 100 or D > 100:
    sys.exit()

count = 0
for I in range(A,B):
    for J in range(C,D):
        if I == J:
            count += 1
print(count)