A, B, C, D = map(int, input().split())
Alice = [int(i) for i in range(A,B)]
Bob = [int(i) for i in range(C,D)]
print(len(set(Alice) & set(Bob)))