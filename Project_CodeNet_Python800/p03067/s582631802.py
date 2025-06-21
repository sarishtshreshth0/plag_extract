A, B, C = map(int, input().split())

count = 0
if A > B:
    for i in range (B, A):
        if i == C:
            count = 1
elif A < B:
    for i in range (A, B):
        if i == C:
            count = 1

if count == 1:
    print("Yes")
else:
    print("No")