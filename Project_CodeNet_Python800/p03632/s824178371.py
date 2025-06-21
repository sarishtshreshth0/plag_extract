A, B, C, D = map(int, input().split())

range_AB = range(A, B + 1)
range_CD = range(C, D + 1)

if set(range_AB) & set(range_CD):
    print(len(set(range_AB) & set(range_CD)) - 1)
else:
    print(0)
