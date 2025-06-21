A, B, C = map(int, input().split())

# print(A)
# print(B)
# print(C)

if A <= C and C <= B:
    print('Yes')
elif A >= C and C >= B:
    print('Yes')
else:
    print('No')