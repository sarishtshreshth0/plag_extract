A, B, C, D = map(int, input().split())
print(len(set([i for i in range(A, B)]) & set([i for i in range(C, D)])))
