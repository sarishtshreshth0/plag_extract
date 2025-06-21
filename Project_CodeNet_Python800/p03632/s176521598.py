A, B, C, D = map(int, input().split())

alice = [0]*100
bob = [0]*100

alice[A:B] = [1]*(B-A)
bob[C:D] = [1]*(D-C)

print(sum([alice[i]*bob[i] for i in range(100)]))